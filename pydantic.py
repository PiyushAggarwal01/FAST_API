from pydantic import BaseModel ,EmailStr, AnyUrl, Field
from typing import List ,Dict, Optional, Annotated

class patient(BaseModel):
    name : Annotated[str, Field( max_length=50, tittle = 'name of the patient', description='give the name of the patient in less than 50 words ')]
    email : EmailStr
    linkedin_url : AnyUrl
    age: Annotated[int , Field(gt=0, lt=120, title='age of the patient ', )]