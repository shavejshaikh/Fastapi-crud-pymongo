import uvicorn
from fastapi import FastAPI
from app.config.settings import settings
from app.controllers import include_routers

app = FastAPI(title="FastAPI crud mongodb")

@app.get("/")
def home():
    context = {
        "MONGOBG_URL" : settings.MONGODB_URL,
        "MONGODB_DATABASE": settings.MONGODB_DATABASE
    }
    return context


include_routers(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8000, reload=True)