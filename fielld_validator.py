from pydantic import BaseModel, EmailStr, anyurl , field , field_validator
from typing import list , Dict , optimal , Annotated

class Patient(BaseModel):
    
    name : str
    Email:EmailStr
    age :int 
    weight : float
    married : bool
    allergies : list[str]
    contact_detail: Dict[str, str]
    
@field_validator('email')
@classmethod
def email_validator(cls, value):
    valid_domain : ['hdfc.com', 'icici.com']
    domain_name :value.split('@')[-1]
    if value  not in domain_name:
       raise ValueError('not a valid domain')
    return value

    
    