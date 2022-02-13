import uvicorn
from fastapi import FastAPI
from routers.research import research

app = FastAPI()
app.include_router(research.router)


@app.get('/')
async def root():
    return {'key': 'Hello'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
