import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from collections import Counter

import text_configs 

# Определим тип данных для каждых фичей
# Это необходимо, для того, чтобы искать выбросы по числовым и категориальным
def get_features_types(db: pd.DataFrame) -> dict:
    features = {'numeric': [], 'text_object': [], 
                'categorial': [], 'datetime': [], 'boolean': []}
    for col in db.columns:
        if db[col].dtype == "object":
            if len(db[col].unique()) >= len(db) * 0.2:
                features['text_object'].append(col)
            else:
                features['categorial'].append(col)
        elif db[col].dtype == "int64" or db[col].dtype == "float64":
            features['numeric'].append(col)
        elif db[col].dtype == "datetime64":
            features['datetime'].append(col)
        elif db[col].dtype == "bool":
            features['boolean'].append(col)
    return features

# Оставляем только категориальные и числовые фичи
def preprocesing_data(db: pd.DataFrame) -> pd.DataFrame:
    db_copy = db.copy()
    f_type = get_features_types(db)

    for col in f_type['categorial']:
        db_copy[col] = db_copy[col].fillna("None")
        le = preprocessing.LabelEncoder()
        le.fit(db_copy[col])
        db_copy[col] = le.transform(db_copy[col])

    for col in f_type['numeric']:
        db_copy[col] = db_copy[col].fillna(db_copy[col].mean())

    cat_lst = f_type['numeric'] + f_type['categorial']
    return db_copy[cat_lst]

# Считаем изолированные лес (выявляет неоднородности)
def get_iso(db: pd.DataFrame) -> list:
    iso = IsolationForest(contamination=0.01)
    yhat_iso = iso.fit_predict(db)
    return yhat_iso == -1

# Считаем выбросы из нормального распределения
def get_gauss(db: pd.DataFrame) -> list:
    ee = EllipticEnvelope(contamination=0.01)
    yhat_gaus = ee.fit_predict(db)
    return yhat_gaus == -1

# Считаем неоднородности среди ближайших соседей
def get_lof(db: pd.DataFrame) -> list:
    lof = LocalOutlierFactor()
    yhat_lof = lof.fit_predict(db)
    return yhat_lof == -1

# Считаем one svm для определения новизны в данных
def get_svm(db: pd.DataFrame) -> list:
    ee = OneClassSVM(nu=0.01)
    yhat_svm = ee.fit_predict(db)
    return yhat_svm == -1

def get_outliers(db: pd.DataFrame) -> Counter:
    outliers = pd.DataFrame({'iso': get_iso(db), 
                             'gauss': get_gauss(db), 
                             'lof': get_lof(db), 
                             'svm': get_svm(db)})

    for col in outliers.columns:
        outliers[col] = outliers[col].astype('int64')

    outliers['sum'] = outliers['iso'] + outliers['gauss'] + outliers['lof'] + outliers['svm']
    return Counter(outliers['sum'])


def get_response_for_outliers(db: pd.DataFrame) -> dict:
    '''
    Отчет публикуется всего по одной категории: 
    outliers: рекомендация по тому, стоит ли избавляться от выбросов.
    '''
    response = {"outliers": ""}

    outliers = get_outliers(preprocesing_data(db))

    if outliers[4] > 0 or outliers[3] > 0:
        n = (outliers[4] + outliers[3]) / len(db)
        response["outliers"] = text_configs.outliers_high.format(n * 100)
    elif outliers[2] > 0:
        n = outliers[2] / len(db)
        response["outliers"] = text_configs.outliers_normal.format(n * 100)
    else:
        response["outliers"] = text_configs.outliers_base

    return response