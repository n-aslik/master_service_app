from fastapi import Depends,APIRouter, Response, BackgroundTasks
from ..schemas import schema

from typing import Any
from package.repository import auth_module
from package.service import jwt_hand as JWTHandler


router=APIRouter(prefix="/api/v1/auth",tags=["AUTHORIZATION"])

    
@router.post("/sign-in")
async def login(data: schema.Login = Depends()):
    return await auth_module.login(data)

@router.put('/forgot-password')
async def forgot_password(data: schema.ForgotPassword = Depends() ):
    return await auth_module.forgot_password(data)

@router.put("/change-password")
async def change_password(data: schema.ChangePassword = Depends()):
    return  await auth_module.change_password(data)

@router.post('/refresh/token')
async def refresh_token(response: Response, payload: dict = Depends(JWTHandler.refresh_token)):
    return await auth_module.refresh_token(payload)

@router.delete('/profile')
async def delete_profile(payload: dict = Depends(JWTHandler.access_token)):
    return await auth_module.delete_profile(payload["user_id"])

@router.delete('/logout')
async def logout(payload: dict = Depends(JWTHandler.access_token)):
    return await auth_module.logout(payload['user_id'])


