from fastapi import FastAPI
from src.app import  models
from src.app.database import engine
from src.app.routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()


origins = ["*"]



models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)