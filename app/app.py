from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title=Futurisys ML API)
app.include_router(router)

if __name__ == __main__
    import uvicorn
    uvicorn.run(app, host=0.0.0.0, port=7860)