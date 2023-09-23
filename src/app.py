from fastapi import FastAPI
import uvicorn
from elasticsearchconnection import connectTest

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"message": "Health check!!!"}

@app.get("/connect")
async def connect():
    return {"message": connectTest()}

if __name__ == '__main__':
    uvicorn.run("app:app", port=7777, host='0.0.0.0', reload=True)