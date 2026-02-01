from fastapi import FastAPI, Request

from TodoApp import models
from TodoApp.database import engine
from TodoApp.routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="TodoApp/templates")

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

@app.get("/dima")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


app.include_router(auth.router)
app.include_router(todos.router)

app.include_router(admin.router)

app.include_router(users.router)


