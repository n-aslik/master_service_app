from fastapi import Depends,APIRouter, Response, BackgroundTasks
from ..schemas import schema

from typing import Any
from package.repository import auth_module
from package.service import jwt_hand as JWTHandler


router=APIRouter(prefix="/api/v1/auth",tags=["AUTHORIZATION"])

    
@router.post("/sign-in")
async def login(data: schema.Login = Depends()):
    return await auth_module.login(data)

@router.post('/send-message')
async def send_message(background_tasks: BackgroundTasks, phone:str = Depends()):
    background_tasks.add_task(auth_module.send_message, phone,  message = "Вы изменили свой пароль")
    return {'message':"Сообщение отобразился на фоне"}

@router.put("/change-password")
async def change_password(data: schema.ChangePassword = Depends()):
    return  await auth_module.change_password(data)

@router.post('/refresh/token')
async def refresh_token(response: Response, payload: dict = Depends(JWTHandler.refresh_token)):
    return await auth_module.refresh_token(payload)
