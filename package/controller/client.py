from fastapi import APIRouter,Depends,Path
from ..schemas import schema
from ..repository import client_module
from typing import Optional
from . import middleware
from ..service.jwt_hand import Payloads
router=APIRouter(
    prefix="/api/v1/client",tags=["CLIENT"]

)
@router.post("/client")
async def create_client(data: schema.Client_Model = Depends(), payload: Payloads = Depends(middleware.check_client_autherization) ):
    return await client_module.create_client(data)

@router.put("/client")
async def edit_user(id: int, data:schema.Client_Model = Depends(), payload:Payloads=Depends(middleware.check_client_autherization)):
    return await client_module.update_client(payload["user_id"], data)
    
@router.delete('client')
async def delete_client(id:int, payload: Payloads = Depends(middleware.check_client_autherization)):
    return await client_module.delete_client(payload["user_id"])

@router.get("/client")
async def get_client(id: Optional[int] = None):
    return await client_module.get_client(id)

@router.get('/client-comment')
async def get_client_comment(client_id: Optional[int] = None, payload: Payloads = Depends(middleware.check_master_autherization)):
    return await client_module.get_client_comment(payload["user_id"], client_id)
    
@router.get('/client-orders')
async def get_client_orders(client_id: Optional[int] = None, payload: Payloads = Depends(middleware.check_master_autherization)):
    return await client_module.get_client_orders(client_id)


