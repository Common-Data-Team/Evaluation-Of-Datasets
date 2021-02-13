import re
import uvicorn
from fastapi import FastAPI, File, UploadFile, Body
import pandas as pd
from io import BytesIO
from pydantic import BaseModel
from column_analyzer import get_chart_data


app = FastAPI()
email_template = re.compile('^[^@]+@[^@.]+\.[^@]+$')


class Email(BaseModel):
    email: str


@app.post('/upload/')
def process(file: UploadFile = File(...)):
    df = pd.read_csv(BytesIO(file.file.read()))
    return {'charts': get_chart_data(df)}


@app.post('/email/')
def save_email(email_json: Email = Body(...)):
    email_template.findall(email_json.email)


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
