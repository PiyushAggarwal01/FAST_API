from pydantic import BaseModel, EmailStr, anyurl , field , field_validator
from typing import list , dict , optimal , Annotated

class Patient(BaseModel):
    
    name : str
    Email:EmailStr
    age