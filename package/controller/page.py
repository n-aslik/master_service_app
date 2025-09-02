from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from package.service import jwt_hand as JWTHandler
from package.repository import client_module
from typing import List

templates = Jinja2Templates("package/templates")
router  = APIRouter()

@router.get("/enter_chat", response_class = HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})

@router.post('/join-chat', response_class=HTMLResponse)
async def join_chat(request: Request, first_name: str = Form(...), room_id: int = Form(...), payload: dict = Depends(JWTHandler.access_token)):
    await client_module.update_user_chat(payload["user_id"], first_name, room_id)
    return templates.TemplateResponse("index.html",{"request": request, "room_id": room_id, "first_name": first_name, "user_id": payload["user_id"]})
    