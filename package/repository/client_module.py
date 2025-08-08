from fastapi import HTTPException,status
from database.dbconn import async_get_db
from ..schemas import schema

async def create_client(data: schema.Client_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_client(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" ,
                    ('{}', data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.password,
                           data.email,
                           data.social_nik,
                           data.qr_code))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client(id: int, data: schema.User):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_client(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" ,
                    ('{}', id,
                           data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.email,
                           data.social_nik,
                           data.qr_code
                    ))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def delete_client(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_client(%s, %s);" ,(id, '{}'))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_client(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client(%s);",(id,))
        client = cur.fetchone()[0]
        return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_clients(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_clients(%s);",(id,))
        clients = cur.fetchone()[0]
        return clients
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{clients}")


async def create_client_orders(id: int, data: schema.Client_Orders_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_client_orders(%s, %s, %s, %s);" ,('{}', id, data.deadline, data.orders))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def create_client_comments(id: int, data: schema.Client_Comment_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.get_client_comment(%s, %s, %s, %s, %s);" ,('{}', id, data.master_id, data.rating, data.comment))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client_orders(id: int, data: schema.Client_Orders_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_client_orders(%s, %s, %s, %s);" ,('{}', id, data.deadline, data.orders))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client_comments(id: int, data: schema.Client_Comment_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_client_comment(%s, %s, %s, %s, %s);" ,('{}', id, data.master_id, data.rating, data.comment))
        client = cur.fetchone()[0]
        if client['status'] == 1:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")



async def get_client_comment(master_id: int, client_id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client_comment(%s, %s);" ,(master_id, client_id))
        client = cur.fetchone()[0]
        return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_client_orders(client_id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client_orders( %s );" ,( client_id,))
        client = cur.fetchone()[0]
        return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")


    
    