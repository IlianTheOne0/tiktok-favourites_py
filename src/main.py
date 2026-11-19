from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



from src.api.routes import health



app = FastAPI(
    title="TikTok Collections Manager API",
    version="0.1.0",
    description="Backend for syncing TikTok collections with the mobile app",
)

app.add_middleware(
    CORSMiddleware,
    
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(health.router, prefix="/health", tags=["health"])