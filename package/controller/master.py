from fastapi import APIRouter,Depends,Path,BackgroundTasks
from ..schemas import schema
from ..repository import master_module
from typing import Optional
from . import middleware
from ..service.jwt_hand import Payloads
router=APIRouter(
    prefix="/api/v1/master",tags=["MASTER"]

)

@router.post("/master")
async def create_master(data: schema.Master_Model = Depends() ):
    return  await master_module.create_master(data)

@router.put("/master")
async def update_master(id: int, data:schema.Master_Model = Depends(), payload:Payloads=Depends(middleware.check_master_autherization)):
    return await master_module.update_master(payload["user_id"], data)
    
@router.delete('master')
async def delete_master(id:int, payload: Payloads = Depends(middleware.check_master_autherization)):
    return await master_module.delete_master(payload["user_id"])

@router.get("/master")
async def get_master(id: Optional[int] = None, payload: Payloads = Depends(middleware.check_client_autherization)):
    return await master_module.get_masters(id)

@router.get('/master-position')
async def get_master_position(position_id: Optional[int] = None, cost: Optional[float] = None, payload: Payloads = Depends(middleware.check_client_autherization)):
    return await master_module.get_master_position(position_id, cost)

@router.get('/master-accepted-orders')
async def get_master_accepted_orders(payload: Payloads = Depends(middleware.check_master_autherization)):
    return await master_module.get_master_accepted_orders(payload['user_id'])

   

