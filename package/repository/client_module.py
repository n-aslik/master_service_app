from fastapi import HTTPException,status
from database.dbconn import async_get_db
from ..schemas import schema

async def create_client(data: schema.Client_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_client(%s, %s, %s, %s, %s, %s, %s, %s, %s);" ,
                    ('{}', data.first_name,
                           data.last_name,
                           data.gender,
                           data.birth_date,
                           data.phone_number,
                           data.email,
                           data.social_nik,
                           data.qr_code))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
        elif client["status"] == 1:
            return client["message"]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client(id: str, data: schema.User):
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
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def delete_client(id: str):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.delete_client(%s, %s);" ,(id, '{}'))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_client(id: str):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client_by_id(%s);",(id,))
        client = cur.fetchone()[0]
        return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")


async def create_client_orders(id: str, data: schema.Client_Orders_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.create_clients_orders(%s, %s, %s, %s);" ,( id,  data.orders, data.deadline, '{}'))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def create_client_comments(id: str, data: schema.Client_Comment_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.get_clients_comment(%s, %s, %s, %s, %s);" ,('{}', id, data.rating, data.comment, data.master_id))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client_orders(id: str, data: schema.Client_Orders_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_clients_orders(%s, %s, %s, %s);" ,( id, data.orders,  data.deadline, '{}'))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def update_client_comments(id: str, data: schema.Client_Comment_Model):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.update_clients_comment(%s, %s, %s, %s, %s);" ,('{}', id,  data.rating, data.comment, data.master_id))
        client = cur.fetchone()[0]
        if client['status'] == 0:
            return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")

async def get_client_orders():
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT masters_services.get_client_orders(  );" ,( ))
        client = cur.fetchone()[0]
        return client
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{client}")


    
    