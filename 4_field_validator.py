# field_validator is used to apply custom validation logic on specific fields after basic type checks.
# Feild Validator works in 2 modes
# 1. Before mode(mode='before') - > It will take the value without an type conversion
# 2. After mode(mode='after') - > defualt

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1] #['abc', 'hdfc.com]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a Valid Domain')
        
        return value
    
    @field_validator('age')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")
        
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()



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
update_patient_data(patient1)