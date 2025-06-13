from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icic.com']
        # will extract the @ part of gmail
        domain_name=value.split('@')[-1]

        if domain_name  not in valid_domains:
            raise ValueError ('Not a valid email')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    @field_validator('age',mode='after')
    @classmethod
    def age_valid(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Enter valid age ')
    


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')


patient_info={'name':'krish','email':'abc@hdfc.com','age':'40','weight':80,'link':'http://linkedin.com/123','married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'9784853377'}}
# patient_info={'name':'Krish','age':'thirty'}

patient1=Patient(**patient_info)
#got out pydantic object patient1

#STEP 3
update_patient_data(patient1)