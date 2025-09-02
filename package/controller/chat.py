from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter,Depends
from fastapi.responses import HTMLResponse
from typing import Dict
from package.repository import client_module


class ConnectionManager:
    def __init__(self):
        self.active_connection: Dict[int, Dict[str, WebSocket]] = {}
        
    async def connect(self, websocket: WebSocket, room_id: int, user_id: int ):
        await websocket.accept()
        if room_id not in self.active_connection:
            self.active_connection[room_id] = {}
        self.active_connection[room_id][user_id] = websocket
    
    def disconnect(self, room_id: int, user_id: int):
        if room_id in self.active_connection and user_id in self.active_connection[room_id]:
            del self.active_connection[room_id][user_id]
            if not self.active_connection[room_id]:
                del self.active_connection[room_id]
                
      
    async def broadcast(self, message: str, room_id: int, sender_id: int):
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
async def websocket_endpoint(websocket: WebSocket, room_id:int, user_id: int, firstname: str):
    await manager.connect(websocket, room_id, user_id)
    await manager.broadcast(f"{firstname} (ID: {user_id}) присоединился к чату", room_id, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{firstname} (ID: {user_id}) : {data}", room_id, user_id)
            await client_module.update_user_chat(user_id, firstname, room_id, data)
    except WebSocketDisconnect:
        manager.disconnect(room_id, user_id)
        await manager.broadcast(f"{firstname} (ID: {user_id}) покинул чат", room_id, user_id)
