from pydantic import BaseModel ,EmailStr, AnyUrl, Field
from typing import List ,Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field( max_length=50, tittle = 'name of the patient', description='give the name of the patient in less than 50 words ')]
    email : EmailStr
    linkedin_url : AnyUrl
    age: Annotated[int , Field(gt=0, lt=120,  )]
    weight : Annotated[float, Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    
def update_patient_data(patient:patient):
      print(patient.name)
      print(patient.age)  
      print(patient.allergies)  
      print(patient.married)
      print('updated')
      
patient_info = {'name':'piyush ', 'email':'piyush@gmail.com', 'linkedin_url' :'http://linked.com/1322', 'age':'30', 'weight': 75.2,'contact_details':{'phone':'2353462'}} 

Patient1 = Patient(**patient_info)
update_patient_data(Patient1)
