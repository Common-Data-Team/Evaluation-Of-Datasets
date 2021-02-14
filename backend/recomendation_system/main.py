import pandas as pd
from recomendation_system.missing_data import get_response_for_missing
from recomendation_system.outliers_data import get_response_for_outliers
from recomendation_system.informs_data import get_response_for_informs


def get_response(db: pd.DataFrame) -> dict:
    '''
    Формирование отчета по категориям:
    missings: пропуски в данных, подробнее о структуре описано в missing_data.py,
    
    outliers: выбросы и аномалии в данных, подробнее о структуре описано в outliers_data.py,
    
    informs: информативность данных и дублируемость категориальных признаков,
    подробнее о структуре описано в informs_data.
    '''
    response = {"missings": get_response_for_missing(db),
                "outliers": get_response_for_outliers(db),
                "informs": get_response_for_informs(db)}

    return response
