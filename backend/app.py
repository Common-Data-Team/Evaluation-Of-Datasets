import re
import uvicorn
from fastapi import FastAPI, File, UploadFile, Body
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
def process(file: bytes = File(...)):
    df = pd.read_csv(BytesIO(file))
    return {'charts': get_chart_data(df)}


@app.post('/email')
def save_email(email_json: Email = Body(...)):
    email_template.findall(email_json.email)


@app.get('/ping')
def ping():
    return 'ok'


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
