import pandas as pd
import numpy as np
from collections import Counter

import text_configs 
# Считаем соотношение пропусков по каждой фиче
def get_missing_by_col(db: pd.DataFrame) -> dict:
    dict_missing_by_col = {}
    for col in db.columns:
        pct_missing = np.mean(db[col].isnull())
        #print('{} - {}%'.format(col, round(pct_missing*100)))
        dict_missing_by_col[col] = pct_missing
    return dict_missing_by_col

# will do: сделать мягкую настройку коэффициентов
def get_distrib_missing_by_col(db: pd.DataFrame) -> dict:
    miss_by_col = get_missing_by_col(db)
    miss_20_col = []
    miss_40_col = []
    miss_60_col = []
    for key, value in miss_by_col.items():
        if value >= 0.6:
            miss_60_col.append(key)
        elif value >= 0.4:
            miss_40_col.append(key)
        elif value >= 0.2:
            miss_20_col.append(key)
    return {'missing_20': miss_20_col, 'missing_40': miss_40_col, 'missing_60': miss_60_col}

# Считаем распределение пропусков
def get_missing_by_row(db: pd.DataFrame) -> Counter:
    count_null = np.sum(db_copy.isnull(), axis=1)
    lst_missing_by_row = Counter(count_null)
    #print(lst_missing_by_row)
    return lst_missing_by_row

# will do: сделать мягкую настройку коэффициентов
def get_distrib_missing_by_row(db: pd.DataFrame) -> dict:
    miss_by_row = get_missing_by_row(db)
    per_20 = 0.2 * len(db.columns)
    per_40 = 0.4 * len(db.columns)
    per_60 = 0.6 * len(db.columns)

    light = 0
    normal = 0
    hard = 0
    for i in range(round(per_20), round(per_40) + 1):
        light += miss_by_row[i]
    for i in range(round(per_40) + 1, round(per_60) + 1):
        normal += miss_by_row[i]
    for i in range(round(per_60) + 1, len(db.columns) + 1):
        hard += miss_by_row[i]
    return {'light': light, 'normal': normal, 'hard': hard}

# Считаем распределение пропусков в численных, категориальных, временных, булевых и текстовых данных
def get_features_types(db: pd.DataFrame) -> dict:
    features = {'numeric': [], 'text_object': [], 'categorial': [], 'datetime': [], 'boolean': []}
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

def get_missing_by_features(db: pd.DataFrame) -> dict:
    features = get_features_types(db)
    mising_features = {'numeric': 0, 'text_object': 0, 'categorial': 0, 'datetime': 0, 'boolean': 0}
    for col in db.columns:
        if db[col].dtype == "object":
            if len(db[col].unique()) >= len(db) * 0.2:
                cat_ft = 'text_object'
            else:
                cat_ft = 'categorial'
        elif db[col].dtype == "int64" or db[col].dtype == "float64":
            cat_ft = 'numeric'
        elif db[col].dtype == "datetime64":
            cat_ft = 'datetime'
        elif db[col].dtype == "bool":
            cat_ft = 'boolean'
        mising_features[cat_ft] += np.sum(db[col].isnull())
    for key in mising_features.keys():
        try:
            mising_features[key] /= (len(db) * len(features[key]))
        except ZeroDivisionError:
            mising_features[key] = 0
    return mising_features

# will do: сделать мягкую настройку коэффициентов
def get_distrib_missing_by_features(db: pd.DataFrame) -> dict:
    miss_by_features = get_missing_by_features(db)
    per_20 = []
    per_40 = []
    per_60 = []

    description_dtype = {'numeric': "Числовые данные", 
                         'text_object': "Текстовые и неклассифицируемые данные", 
                         'categorial': "Категориальные данные", 
                         'datetime': "Данные времени и даты", 
                         'boolean': "Булевые данные"}
    for key, value in miss_by_features.items():
        if value >= 0.6:
            per_60.append(description_dtype[key])
        elif value >= 0.4:
            per_40.append(description_dtype[key])
        elif value >= 0.2:
            per_20.append(description_dtype[key])
    return {'missing_20': per_20, 'missing_40': per_40, 'missing_60': per_60}

# Делаем вердикт по пропускам в данных
def get_response_for_missing(db: pd.DataFrame) -> dict:
    '''
    Отчет публикуется по трем категориям: 
    miss_by_col: пропуски по признакам и его зависимости:
      если этот признак не пуст, то в дополнение к отчету публикуем все
      непустые зависимости,
      missed_col_extreme: названия признаков с экстремальной долей пропусков,
      missed_col_normal: названия признаков с нормальной долей пропусков,
      missed_col_low: названия признаков с вполне терпимой долей пропусков;
    miss_by_row: пропуски по строкам; 
    miss_by_dtype: пропуски по типам данных;
    duplicate: наличие дубликатов.
    Если какой-то из ключей отчета пуст - значит данные в этом плане 
    оптимизированы и мы в конечную верстку это не включаем.
    '''
    response = {"miss_by_col": "",
                "missed_col_extreme": [],
                "missed_col_normal": [],
                "missed_col_low": [],
                "miss_by_row": "",
                "miss_by_dtype": "",
                "duplicate": ""}

    miss_by_col = get_distrib_missing_by_col(db)
    miss_by_row = get_distrib_missing_by_row(db)
    miss_by_features = get_distrib_missing_by_features(db)

    if len(miss_by_col['missing_60']) > 0:
        response["miss_by_col"] = text_configs.miss_by_col_extreme 
    elif len(miss_by_col['missing_40']) > 0:
        response["miss_by_col"] = text_configs.miss_by_col_normal
    elif len(miss_by_col['missing_20']) > 0:
        response["miss_by_col"] = text_configs.miss_by_col_low
    
    response["missed_col_extreme"] = miss_by_col['missing_60']
    response["missed_col_normal"] = miss_by_col['missing_40']
    response["missed_col_low"] = miss_by_col['missing_20']

    if miss_by_row['hard'] > 0:
        response["miss_by_row"] += text_configs.miss_by_row_extreme 
    elif miss_by_row['normal'] > 0:
        response["miss_by_row"] = text_configs.miss_by_row_normal

    if len(miss_by_features['missing_60']) > 0:
        txt = text_configs.miss_by_feature_extreme 
        for name in miss_by_features['missing_60']:
            txt += (name + "\n")
        response["miss_by_col"] = txt 
    elif len(miss_by_features['missing_40']) > 0:
        txt = text_configs.miss_by_feature_normal 
        for name in miss_by_features['missing_40']:
            txt += (name + "\n")
        response["miss_by_col"] = txt

    if sum(db.duplicated()) > 0:
        response["duplicate"] = text_configs.duplicate

    return response