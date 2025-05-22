from pydantic import BaseModel
from typing import List, Dict, Optional
class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool = False # setting an default value
    allergies: Optional[List[str]] = None
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

patient_info = {
    'name': 'nikhil',
    'age': 23,
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'email': 'abcd@gmail.com',
        'phone': '2333434'  
    }
}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)