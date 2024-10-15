from fastapi import FastAPI, APIRouter
from routers import category

app = FastAPI()

@app.get("/") 
async def weclome() -> dict:
    return {"message": "Welcome to FastAPI"}

app.include_router(category.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)