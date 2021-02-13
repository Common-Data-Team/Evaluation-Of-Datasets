import re
import uvicorn
from fastapi import FastAPI, File, UploadFile, Body
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from pydantic import BaseModel
from column_analyzer import get_chart_data

app = FastAPI()
email_template = re.compile('^[^@]+@[^@.]+\.[^@]+$')
origins = [
    "http://datasets.commondata.ru",
    "https://datasets.commondata.ru",
    "http://localhost:5000",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Email(BaseModel):
    email: str


@app.post('/upload')
def process(file: UploadFile = File(...)):
    df = pd.read_csv(BytesIO(file.file.read()))
    return {'charts': get_chart_data(df)}


@app.post('/email')
def save_email(email_json: Email = Body(...)):
    email_template.findall(email_json.email)


@app.get('/ping')
def ping():
    return 'ok'


@app.get('/')
def first():
    content = """
    <body>
    <form action="/upload" enctype="multipart/form-data" method="post">
    <input name="file" type="file" multiple>
    <input type="submit">
    </form>
    </body>
        """
    return HTMLResponse(content=content)


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
