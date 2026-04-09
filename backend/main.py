#Imports
from fastapi import FastAPI
from app.routes.users import router
from fastapi.middleware.cors import CORSMiddleware

#app config
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/{rest_of_path:path}")
async def preflight_handler(rest_of_path: str):
    return {}

#app (router API)
app.include_router(router)