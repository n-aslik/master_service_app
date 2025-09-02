from pydantic import BaseModel
from typing import Optional, Dict, List


class User(BaseModel): 
    first_name: str
    last_name: str
    gender: bool
    birth_date: str
    phone_number: Optional[str] = None
    email: Optional[str] = None
    social_nik: Optional[str] = None
    qr_code: Optional[str] = None



class Client_Model(User):
    pass
    
class Service_Type_Model(BaseModel):
    type: str
    cost: float
    
class PositionModel(BaseModel):
    name: str
    service_type_id: int

class Master_Model(User):
    experience: int
    position_id: Optional[List[int]] = None
    
class Client_Comment_Model(BaseModel):
    rating: Optional[int] = None
    comment: Optional[List[str]] = None
    master_id: int

class Client_Orders_Model(BaseModel):
    orders: List[str]
    deadline: str
    
class Login(BaseModel):
    phone_number: str
    password: str
    
class ForgotPassword(BaseModel):
    phone_number:str
    
    
class ChangePassword(Login):
    new_password: str
    

