from fastapi import FastAPI,Request,HTTPException
from fastapi.staticfiles import StaticFiles
import time
from database.dbconn import async_get_db
from package.controller.client import router as client_router
from package.controller.master import router as master_router
from package.controller.auth import router as auth_router
from package.controller.chat import router as chat_router
from package.controller.page import router as page_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Master`s Services")

async def get_db():
    try:
        db =  async_get_db()
        curs = db.cursor()
        yield curs
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        raise HTTPException(status_code=409, detail="db error: {}".format(e))
    finally:
        curs.close()
        
        
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-App"] = "Time took to process the request and return response is {} sec".format(time.time() - start_time)
    return response


app.mount("/static", StaticFiles(directory="package/static"), 'static')
app.include_router(client_router)
app.include_router(master_router)
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(page_router)
        
