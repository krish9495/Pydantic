from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property 
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi





def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.bmi)
    print('inserted')


patient_info={'name':'krish','email':'abc@hdfc.com','age':70,'weight':80,'link':'http://linkedin.com/123','married':True,'height':1.7,'allergies':['pollen','dust'],'contact_details':{'phone':'9784853377','emergency':'100'}}
# patient_info={'name':'Krish','age':'thirty'}

patient1=Patient(**patient_info)
#got out pydantic object patient1

#STEP 3
update_patient_data(patient1)
