#Pydantic helps us to resolve 2 problems
#1. Type Validation
#2. Data Validation

def insert_patient_data(name: str, age: int): # name:str - > Type hinting

    if type(name) == str and type(age) == int: #This Type Validation is not a production grade code 
        if age < 0 :
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print("Inserted in the DB")
    else:
        raise TypeError("Incorrect Type")

def update_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:

        if age < 0:
            raise ValueError('Age cannot be negative') # This is called an Data Validation 
        else:
            print(name)
            print(age)
            print("Updated in the DB")
    else:
        raise TypeError("Incorrect data type")



insert_patient_data('nikhil', '30')