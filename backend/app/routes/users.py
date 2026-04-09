# Imports
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import List
from ..db.crud import create_user_db, get_users_db, update_user_db, delete_user_db, get_users_name_db
from ..schemas.user import User, UserRespose
from ..security.hash_pwd import hashed, verify_hash
from ..security.token_security import create_token, verify_token

#app (router API)
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(401, "Invalid Token")

    return payload

# Endpoint Main
@router.get("/")
def home():
    return {"message": "Hello, User!"}

# Endpoint Create
@router.post("/users", status_code=201)
def create_user(user: User):
    password_hashed = hashed(user.password)
    user_db_id = create_user_db(user.name, password_hashed)

    if not user_db_id:
        return HTTPException(status_code=400, detail="Invalid data.")
    
    return {"datail": "Created User!"}

# Endpoint Read
@router.get("/users", response_model=List[UserRespose])
def get_users():
    users = get_users_db()

    if not users:
        return HTTPException(status_code=404, detail="Users not found.")
    return users

# Endpoint Update
@router.put("/users/{id}")
def update_user(id: int, user: User):
    password_hashed = hashed(user.password)
    result = update_user_db(id, user.name, password_hashed)

    if result == 0:
        return HTTPException(status_code=404, detail="User not Found")

    return {"datail": "Updated user!"}

# Endpoint Delete
@router.delete("/users/{id}")
def delete_user(id: int, user_p:User = Depends(get_current_user)):
    user = delete_user_db(id)

    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    
    return {"datail": "Deleted user!"}

# Endpoint Login
@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = get_users_name_db(form.username)

    if not user:
        raise HTTPException(status_code=401, detail="User Not Found")
    
    if not verify_hash(form.password, user["password"]):
        raise  HTTPException(status_code=401, detail="Incorrect credentials")
    
    token = create_token({"sub": user["name"]})

    return {"access_token": token, "token_type": "bearer"}