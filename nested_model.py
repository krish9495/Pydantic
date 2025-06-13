from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'city':'banswara','state':'Rajasthan','pincode':327001}
address1=Address(**address_dict)

patient_dict={'name':'Krish','gender':'male','age':20,'address':address1}

patient1=Patient(**patient_dict)
print(patient1)

