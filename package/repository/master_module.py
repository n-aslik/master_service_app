from fastapi import HTTPException,status
from database.dbconn import async_get_db
from ..schemas import schema
# region MASTER

async def create_master(data: schema.Master_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_masters(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    ('{}', data.experience,
                           data.service_type_id,
                           data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.password,
                           data.email,
                           data.social_nik,
                           data.qr_code,
                           data.position_id))
        master = cur.fetchone()[0]
        if master['status'] == 1:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def update_master(id: int, data: schema.Master_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_masters(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    ('{}', id, 
                           data.experience,
                           data.service_type_id,
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
        if master['status'] == 1:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def delete_master(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_master(%s, %s);",(id, '{}'))
        master = cur.fetchone()[0]
        if master['status'] == 1:
            return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")

async def get_masters(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_master(%s);",(id,))
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

async def accepted_orders(client_id: int, master_id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.accepted_orders(%s, %s, %s);", (client_id, master_id, '{}' ))
        master = cur.fetchone()[0]
        return master
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{master}")
 
 
async def get_master_accepted_orders(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_master_accepted_orders(%s);",(id,))
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
        if serv['status'] == 1:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def update_service_type(id: int, data: schema.Service_Type_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_service_type(%s, %s, %s, %s);",(id, data.type, data.cost, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 1:
            return serv
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{serv}")

async def delete_service_type(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_service_type(%s, %s);",(id, '{}'))
        serv = cur.fetchone()[0]
        if serv['status'] == 1:
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