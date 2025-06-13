from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# STEP 1 DEFINING SCHEMA
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the Patient',description='give the name of the patient in less than 50 characters',examples=['Krish Jain','Avani Jain'])]                                           # name:str=Field(max_length=50)-> data validation
    email:EmailStr #this is used for data validation else we need to use regular expression for validating email address but with the special data type of pydantic EmailSTR we can validate
    age:int
    weight:float=Field(gt=0)  #custom data validation using Field Function
    link:AnyUrl
    married:Optional[bool]
    allergies:Optional[List[str]]=None
    # contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')
# STEP 2
patient_info={'name':'Krish','email':'abc@gmail.com','age':21,'weight':80,'link':'http://linkedin.com/123','married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'9784853377'}}
# patient_info={'name':'Krish','age':'thirty'}

patient1=Patient(**patient_info)
#got out pydantic object patient1

#STEP 3
insert_patient_data(patient1)



