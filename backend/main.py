from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# CREATE APP FIRST ✅
app = FastAPI(title="TalentMatch AI")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IMPORT ROUTERS AFTER APP (important order)
from app.routes.analyze import router as analyze_router
from app.routes.recommend import router as recommend_router

# INCLUDE ROUTES
app.include_router(analyze_router)
app.include_router(recommend_router)


@app.get("/")
def home():
    return {"message": "TalentMatch AI Running"}