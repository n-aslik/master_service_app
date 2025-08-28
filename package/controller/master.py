from fastapi import APIRouter,Depends
from ..schemas import schema
from ..repository import master_module
from typing import Optional
from ..service import jwt_hand as JWTHandler
router=APIRouter(
    prefix="/api/v1/master"

)
# region MASTER

@router.post("/master", tags = ['MASTERS'])
async def create_master(data: schema.Master_Model = Depends() ):
    return  await master_module.create_master(data)

@router.put("/master", tags = ['MASTERS'])
async def update_master(id: int, data:schema.Master_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await master_module.update_master(payload["user_id"], data)
    
@router.delete('/master', tags = ['MASTERS'])
async def delete_master(payload:dict=Depends(JWTHandler.access_token)):
    return await master_module.delete_master(payload["user_id"])

@router.get("/master", tags = ['MASTERS'])
async def get_master(id, payload: dict= Depends(JWTHandler.access_token)):
    return await master_module.get_masters(id)

@router.post('/accepted-orders', tags = ['MASTERS'])
async def accepted_orders(client_id, payload: dict = Depends(JWTHandler.access_token)):
    return await master_module.accepted_orders(client_id, payload["user_id"])

@router.get('/master-accepted-orders', tags = ['MASTERS'])
async def get_master_accepted_orders(payload:dict=Depends(JWTHandler.access_token)):
    return await master_module.get_master_accepted_orders(payload["user_id"])

# endregion

# region Service Type

@router.post("/service-type", tags = ["SERVICE-TYPE"])
async def create_service_type(data: schema.Service_Type_Model = Depends(), payload:dict=Depends(JWTHandler.access_token) ):
    return  await master_module.create_service_type(data)

@router.put("/service-type", tags = ["SERVICE-TYPE"])
async def update_service_type(id: int, data:schema.Service_Type_Model = Depends(), payload:dict=Depends(JWTHandler.access_token)):
    return await master_module.update_service_type(id,  data)
    
@router.delete('/service-type', tags = ["SERVICE-TYPE"])
async def delete_service_type(id:int, payload:dict=Depends(JWTHandler.access_token)):
    return await master_module.delete_service_type(id)

@router.get("/service-type", tags = ["SERVICE-TYPE"])
async def get_service_type(payload: dict= Depends(JWTHandler.access_token)):
    return await master_module.get_service_type()

# endregion

# region POSITION

@router.post('/position', tags = ["POSITION"])
async def create_position(data: schema.PositionModel, payload: dict= Depends(JWTHandler.access_token)):
    return await master_module.create_position(data)

@router.delete('/position', tags = ["POSITION"])
async def delete_position(id: int, payload: dict= Depends(JWTHandler.access_token)):
    return await master_module.delete_position(id)

@router.get('/position', tags = ["POSITION"])
async def get_position(payload: dict= Depends(JWTHandler.access_token)):
    return await master_module.get_position()
# endregion

   

