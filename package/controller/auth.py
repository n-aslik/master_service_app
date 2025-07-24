from fastapi import Depends,APIRouter, Response, BackgroundTasks
from ..schemas import schema

from typing import Any
from package.repository import auth_module
from package.service import jwt_hand as JWTHandler


router=APIRouter(prefix="/api/v1/auth",tags=["AUTHORIZATION"])

    
@router.post("/sign-in")
async def login(users: schema.Login):
    return await auth_module.login(users)

@router.post('/send-message')
async def send_message(phone:str, background_tasks: BackgroundTasks):
    background_tasks.add_task(auth_module.send_message, phone,  message = "Вы изменили свой пароль")
    return {'message':"Сообщение отобразился на фоне"}

@router.put("/change-password")
async def change_password(phone: str, password:str, new_password: str):
    return  await auth_module.change_password(phone, password, new_password)


@router.post('/refresh/token')
async def refresh_token(response: Response, payload: dict = Depends(JWTHandler.refresh_token)):
    return await auth_module.refresh_token(payload)
