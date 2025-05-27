# We can export Pydantic data models objects in 2 Formats
# 1. Json(object.model_dump_json())
# 2. Dictionary(object.model_dump())
# Pydantic also gives us a Freedom what we are wanted to ecxport using the keywords:
# include, exclude, exclude_unset


from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))