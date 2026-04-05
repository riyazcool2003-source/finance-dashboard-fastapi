from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# import models so tables are created
from app.models import models

# import route files directly
from app.routes import user_routes
from app.routes import auth_routes
from app.routes import transaction_routes
from app.routes import dashboard_routes
from app.routes import admin_routes


# create FastAPI app
app = FastAPI(
    title="Finance Dashboard API",
    version="1.0.0"
)


# CORS configuration
origins = [

    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",

    "https://your-frontend.com"
]


app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# create database tables
Base.metadata.create_all(bind=engine)


# register routes
app.include_router(user_routes.router)

app.include_router(auth_routes.router)

app.include_router(transaction_routes.router)

app.include_router(dashboard_routes.router)

app.include_router(admin_routes.router)


# root test
@app.get("/")
def root():

    return {
        "message": "Finance API working"
    }