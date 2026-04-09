# Imports
from pydantic import BaseModel, Field

#Schemes User / User Response
class User(BaseModel):
    name: str = Field(min_length=3)
    password: str = Field(min_length=4)

class UserRespose(BaseModel):
    id: int
    name: str