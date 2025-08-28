from fastapi import APIRouter,Depends,Path
from ..schemas import schema
from ..repository import client_module
from typing import Optional
from ..service import jwt_hand as JWTHandler
router=APIRouter(
    prefix="/api/v1/client",tags=["CLIENT"]

)
@router.post("/client")
async def create_client(data: schema.Client_Model = Depends()):
    return await client_module.create_client(data)

@router.put("/client")
async def edit_user(data:schema.Client_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await client_module.update_client(payload["user_id"], data)
    
@router.delete('client')
async def delete_client(id:int, payload: dict = Depends(JWTHandler.access_token)):
    return await client_module.delete_client(payload["user_id"])

@router.get("/client")
async def get_client(payload: dict = Depends(JWTHandler.access_token)):
    return await client_module.get_client(payload["user_id"])

@router.post('/client-comment')
async def create_client_comment(data: schema.Client_Comment_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await client_module.create_client_comments(payload["user_id"], data)
    
@router.post('/client-orders')
async def create_client_orders(data:schema.Client_Orders_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await client_module.create_client_orders(payload["user_id"], data)

@router.put('/client-orders')
async def get_client_orders(data: schema.Client_Orders_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await client_module.update_client_orders(payload["user_id"], data)

@router.get('/client-orders')
async def get_client_orders( payload:dict=Depends(JWTHandler.access_token)):
    return await client_module.get_client_orders()


