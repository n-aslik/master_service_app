from fastapi import HTTPException,status
from database.dbconn import async_get_db
from ..schemas import schema
# region MASTER

async def create_master(data: schema.Master_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_master(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    ('{}', data.experience,
                           data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.email,
                           data.social_nik,
                           data.qr_code,
                           data.position_id))
        master = cur.fetchone()[0]
        if master['status'] == 0:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def update_master(id: str, data: schema.Master_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_master(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    ('{}', id, 
                           data.experience,
                           data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.email,
                           data.social_nik,
                           data.qr_code,
                           data.position_id))
        master = cur.fetchone()[0]
        if master['status'] == 0:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def delete_master(id: str):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_master(%s, %s);" ,(id, '{}'))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_masters():
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_masters(%s);",())
        master = cur.fetchone()[0]
        return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def get_master_position(position_id: int, cost: float):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_masters_position(%s, %s);",(position_id, cost))
        master = cur.fetchone()[0]
        return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def accepted_orders( master_id: str):
    
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.accepted_order(%s, %s);", ( master_id, '{}' ))
        master = cur.fetchone()[0]
        if master["status"] == 0:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")
 
 
async def get_master_accepted_orders(id: str):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client_orders_by_master(%s);",(id,))
        master = cur.fetchone()[0]
        return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")
 

# endregion

# region SERVICE TYPE

async def create_service_type(data: schema.Service_Type_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_service_type(%s, %s, %s);",(data.type, data.cost, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 0:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def update_service_type(id: int, data: schema.Service_Type_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_service_type(%s, %s, %s, %s);",(id, data.type, data.cost, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 0:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def delete_service_type(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_service_type(%s, %s);",(id, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 0:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def get_service_type():
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_service_type();",())
        serv = cur.fetchone()[0]
        return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

# endregion

# region POSITION 

async def create_position(data: schema.PositionModel):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_position(%s, %s, %s);",(data.name, data.service_type_id, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 0:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")


async def delete_position(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_position(%s, %s);",(id, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 0:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def get_position():
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_position();",())
        serv = cur.fetchone()[0]
        return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")


# endregion