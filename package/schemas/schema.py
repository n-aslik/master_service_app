from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel): 
    first_name: str
    last_name: str
    gender: bool
    birth_date: str
    phone_number: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    social_nik: Optional[str] = None
    qr_code: Optional[str] = None

    

class Client_Model(User):
    pass
    
class Service_Type_Model(BaseModel):
    type: str
    cost: float

class Master_Model(User):
    experience: int
    service_type_id: Optional[int] = None
    position_id: Optional[List[int]] 
    
class Client_Comment_Model(BaseModel):
    client_id: int
    comment: Optional[List[str]] = None
    rating: Optional[int] = None
    master_id: int

class Client_Orders_Model(BaseModel):
    client_id:int 
    orders: Optional[List[str]] = None
    deadline: Optional[str] = None
    
class Login(BaseModel):
    phone_number: str
    password: str
    
class ForgotPassword(BaseModel):
    phone_number:str



   
