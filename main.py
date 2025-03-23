from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import process, stream

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(process.router)
api.include_router(stream.router)

@api.get("/")
async def health_check():
    return {"status": "healthy"}