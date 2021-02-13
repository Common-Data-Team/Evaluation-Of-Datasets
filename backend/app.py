import uvicorn
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO
from column_analyzer import get_chart_data


app = FastAPI()


@app.post('/upload/')
def process(file: UploadFile = File(...)):
    df = pd.read_csv(BytesIO(file.file.read()))
    return {'charts': get_chart_data(df)}


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
