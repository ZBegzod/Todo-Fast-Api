from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apps.accounts.models import Base
from config.database import engine
import uvicorn

app = FastAPI(debug=True)
Base.metadata.create_all(bind=engine)


@app.get('/', tags=['Home'])
async def home():
    return "Welcome Home"


app.mount("/static", StaticFiles(directory="static"), name="static")
# app.include_router(auth.router, prefix="/login", tags=["login"])
# app.include_router(loginapp.router, tags=["auth"])


if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, host='127.0.0.1', reload=True)
