from fastapi import HTTPException,status, Response
from database.dbconn import async_get_db
from ..service.jwt_hand import generate_jwt_token
from ..schemas import schema

async def change_password(data: schema.ChangePassword):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.change_password(%s, %s, %s, %s);" ,(data.phone_number, data.password, data.new_password, '{}'))
        users = cur.fetchone()[0]
        if users['status'] == 1:
            return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{users}")

async def login(data: schema.Login):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("CALL masters_services.login(%s, %s, %s);" ,(data.phone_number, data.password, '{}'))
        user = cur.fetchone()[0]
        if user['status'] == 1:
            user['access_token'] = generate_jwt_token(1, user['id'], data.phone_number, user['role'] )
            user['refresh_token'] = generate_jwt_token(2, user['id'], data.phone_number, user['role'])
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{user}")
 
async def refresh_token(payload):
    access_token = generate_jwt_token(1, payload["user_id"], payload["phone"], payload["role"])
    refresh_token = generate_jwt_token(2, payload["user_id"], payload["phone"], payload["role"])
    return {
        'status': 1,
        'user_id': payload["user_id"],
        'access_token': access_token,
        'refresh_token': refresh_token
        
    }
    
async def logout(id: int):
    with async_get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT  masters_services.logout(%s, %s);", (id, '{}'))
        users = cur.fetchone()[0]
        return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{users}")
      
    
def send_message(phone: str, message = "" ):
    with open('message.txt','w', encoding = "UTF-8") as file:
        file.write(f" {phone} {message}")

    
