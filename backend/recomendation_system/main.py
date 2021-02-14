import pandas as pd
from missing_data import get_response_for_missing
from outliers_data import get_response_for_outliers

def get_response(db: pd.DataFrame) -> dict:
    '''
    Формирование отчета по категориям:
    missings: пропуски в данных, подробнее о структуре описано в missing_data.py,
    outliers: выбросы и аномалии в данных, подробнее о структуре описано в outliers_data.py.
    '''
    response = {"missings": get_response_for_missing(db),
                "outliers": get_response_for_outliers(db)}

    return response