# Better organization of related data (e.g., vitals, address, insurance)
# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)
# Readability: Easier for developers and API consumers to understand
# Validation: Nested models are validated automatically—no extra work needed

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nikhil', 'gender': 'male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.gender)
print(patient1.address.city)
print(patient1.address.pin)