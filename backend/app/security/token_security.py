from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "mi_clave_xd"
ALGORITHM = "HS256"

def create_token(data: dict):
    data_copy = data.copy()
    exp = datetime.utcnow() + timedelta(minutes=10)

    data_copy.update({"exp": exp})
    
    token = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None