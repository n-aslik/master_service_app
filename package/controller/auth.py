from fastapi import Depends,APIRouter, Response
from ..schemas import schema
from typing import Any
from package.repository import auth_module
from package.service.jwt_hand import create_refresh_token


router=APIRouter(prefix="/api/v1/auth",tags=["AUTHORIZATION"])

    
@router.post("/sign-in")
async def login(users: schema.Login):
    return await auth_module.login(users)

@router.put("/change-password")
async def change_password(phone:str, password:str, new_password: str):
    return await auth_module.change_password(phone, password, new_password)

@router.post('/refresh/token')
async def refresh_token(response: Response, payload: dict = Depends(create_refresh_token)):
    return await auth_module.refresh_token(payload)
