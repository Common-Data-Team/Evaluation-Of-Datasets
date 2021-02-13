import re
import uvicorn
from fastapi import FastAPI, File, UploadFile, Body, HTTPException
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from pydantic import BaseModel
from column_analyzer import get_chart_data
from recomendation_system.missing_data import get_response_for_missing
from google_sheets import paste_email

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
    chart_data = get_chart_data(df)
    rec_data = get_response_for_missing(df)
    return {'charts': chart_data, 'info': rec_data}


@app.post('/email')
def save_email(email_json: Email = Body(...)):
    email_list = email_template.findall(email_json.email)
    if email_list:
        paste_email(email_list[0])
        return 'ok'
    raise HTTPException(400, 'Invalid email')


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
