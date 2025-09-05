from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter,Depends
from fastapi.responses import HTMLResponse
from typing import Dict
from package.repository import client_module
from package.service import jwt_hand as JWTHandler

bearer = JWTHandler.JWTTokenBearer()

class ConnectionManager:
    def __init__(self):
        self.active_connection: Dict[int, Dict[str, WebSocket]] = {}
        
    async def connect(self, websocket: WebSocket, room_id: int, user_id: str ):
        await websocket.accept()
        if room_id not in self.active_connection:
            self.active_connection[room_id] = {}
        self.active_connection[room_id][user_id] = websocket
    
    def disconnect(self, room_id: int, user_id: str):
        if room_id in self.active_connection and user_id in self.active_connection[room_id]:
            del self.active_connection[room_id][user_id]
            if not self.active_connection[room_id]:
                del self.active_connection[room_id]
                
      
    async def broadcast(self, message: str, room_id: int, sender_id: str):
        if room_id in self.active_connection:
            for user_id, connection in self.active_connection[room_id].items():
                message_with_class = {
                    'text': message,
                    'is_self':user_id == sender_id
                }
                await connection.send_json(message_with_class)


   

router = APIRouter(prefix="/ws/chat")
manager = ConnectionManager()


@router.websocket("/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id:int,  firstname: str, token: str = Depends(bearer)):
    payload = bearer.verify_jwt(token)
    await manager.connect(websocket, room_id, payload["user_id"])
    await manager.broadcast(f"{firstname} (ID: {payload["user_id"]}) присоединился к чату", room_id, payload["user_id"])
    try:
        while True:
            data = await websocket.receive_text()
            await client_module.update_user_chat(payload["user_id"], firstname, room_id, data)
            await manager.broadcast(f"{firstname} (ID: {payload['user_id']}) : {data}", room_id, payload["user_id"])
    except WebSocketDisconnect:
        manager.disconnect(room_id, payload["user_id"])
        await manager.broadcast(f"{firstname} (ID: {payload["user_id"]}) покинул чат", room_id, payload["user_id"])
