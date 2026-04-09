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
@classmethod
def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    
@field_validator('name')
@classmethod
def transform_name(cls, value):
        return value.upper()
@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def update_patient(patient.Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.updated)
     
patient_info = {'name':'piyush','email':'piyush@icici.com', 'age':19, 'weight':55.250, 'married ': False ,'allergies': ['no disease'], 'conatact_detail':{'phone':'7526980703'} }
patient2  = Patient(**patient_info)
update_patient(patient2)