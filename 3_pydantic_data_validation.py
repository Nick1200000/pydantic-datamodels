"""""We can do Data Validation through the various methods 
1. Custom Data Type (EmailStr, AnyUrl)
2. Field(
        We can do 3 things with the field is:
        1. Custom Validation(setting a condtion for data validation)
        2. Setting a metadata 
        3. Setting a defualt values
        Note: Strict=True means we are telling pydantic to not do automatic type conversion   
)"""""

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: Annotated(str, Field(max_length=50, title='Name of the Patient', description='Give me the name of the patients under 50 characters', examples=['Anuj', 'Nikhil'])) #type: ignore
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    linkedin_url: AnyUrl
    # weight: float
    # married: bool = False # setting an default value
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted in the DB")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated Successfully")



patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)