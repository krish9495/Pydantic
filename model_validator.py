from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('must have emergency contact')
        return model




def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')


patient_info={'name':'krish','email':'abc@hdfc.com','age':70,'weight':80,'link':'http://linkedin.com/123','married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'9784853377','emergency':'100'}}
# patient_info={'name':'Krish','age':'thirty'}

patient1=Patient(**patient_info)
#got out pydantic object patient1

#STEP 3
update_patient_data(patient1)