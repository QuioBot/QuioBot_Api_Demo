from fastapi import FastAPI
from src.app import  models
from src.app.database import engine
from src.app.routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1",
    "http://188.166.193.23/#/",
    "http://188.166.193.23/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)