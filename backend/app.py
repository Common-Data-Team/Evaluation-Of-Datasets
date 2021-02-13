import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post('/upload')
def process():
    pass


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
