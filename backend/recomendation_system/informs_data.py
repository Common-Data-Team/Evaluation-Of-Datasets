import pandas as pd
import numpy as np
from nltk.metrics import edit_distance
from collections import Counter
import recomendation_system.text_configs

# Считаем неинформативные признаки
# will do: сделать мягкое определение коэффициента
def get_low_informative_cols(db: pd.DataFrame) -> list:
    df = db.copy()

    num_rows = len(df.index)
    low_information_cols = [] #

    for col in df.columns:
        cnts = df[col].value_counts(dropna=False)
        top_pct = (cnts/num_rows).iloc[0]
    
        if top_pct > 0.9:
            low_information_cols.append(col)
    return low_information_cols

# Считаем уникальные значения в категориальных признаках, которые одинаковые, но
# находятся в разном регистре.
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

def get_dupicate_in_category(db: pd.DataFrame) -> list:
    f_db = get_features_types(db)

    dup_cats = []
    for col in f_db['categorial']:
        cats_name = Counter([str(i).lower() for i in db[col].dropna().unique()])
        if cats_name.most_common(1)[0][1] > 1:
            dup_cats.apend(col)

    return dup_cats

# Считаем уникальные значения в категориальных признаках, вероятно, содержат
# опечатки
def get_mistakes_in_category(db: pd.DataFrame) -> list:
    f_db = get_features_types(db)

    mist_cats = []
    for col in f_db['categorial']:
        cats_name = [str(i).lower() for i in db[col].dropna().unique()]
        for cat in cats_name:
            flag = False
            cur_cat = cats_name.copy()
            cur_cat.remove(cat)
            for i in map(lambda x: edit_distance(x, cat), cur_cat):
                if i <= 1:
                    mist_cats.append(col)
                    flag = True
                    break
            if flag:
                break

    return mist_cats

def get_response_for_informs(db: pd.DataFrame) -> dict:
    '''
    Отчет публикуется по трем категориям. Если категория пуста, значит с данными 
    все ок: 
    non_inforamative: рекомендация по тому, насколько информативны данные, 
    зависимости:
      list_non_informative: список признаков, которые не информативны;
    duplicate_in_category: рекомендация по дубликатам в категориях, зависимости:
      list_col_with_duplicate: список признаков, в которых есть дубликаты кат.;
    '''
    response = {"non_inforamative": "",
                "list_non_informative": [],
                "duplicate_in_category": "",
                "list_col_with_duplicate": []}

    inf_db = get_low_informative_cols(db)
    dup_db = get_dupicate_in_category(db)
    mist_db = get_mistakes_in_category(db)

    dup_db = dup_db + mist_db
    if len(inf_db) > 0:
        response["non_inforamative"] = text_configs.non_informs
        response["list_non_informative"] = text_configs.inf_db
    if len(dup_db) > 0:
        response["duplicate_in_category"] = text_configs.dup_cat
        response["list_col_with_duplicate"] = text_configs.dup_db

    return response
