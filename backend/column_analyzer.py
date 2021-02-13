from collections import Counter
import pandas as pd

sep_symbols = [';', ',', '\t', '.', '/', '\\']


def check_bigtext(series):
    pass


def value_counts(column):
    c = Counter()
    for row in column:
        if isinstance(row, float):
            continue
        for name in row:
            c[name] += 1
    return pd.Series(c)


def check_categories(series):
    return len(series.unique()) <= 20


def get_separator(series):
    sep_symbols = ';,'
    scores = {}
    for symbol in sep_symbols:
        scores[symbol] = 0
        counted_symbol = series.str.count(symbol)
        if len(counted_symbol.unique()) < 2:
            continue

        if counted_symbol.max() != counted_symbol.min():
            scores[symbol] += 2
        vc = counted_symbol.value_counts()
        if (vc[counted_symbol.max()] / len(counted_symbol) < 0.1) or (
                vc[counted_symbol.min()] / len(counted_symbol) < 0.1):
            scores[symbol] -= 2

        if (vc[counted_symbol.max()] / len(counted_symbol) < 0.8) and \
                (vc[counted_symbol.min()] / len(counted_symbol) < 0.8) and (len(vc) > 2):
            scores[symbol] += 3
        # TODO Add more criteria
    res = list(filter(lambda pair: pair[1] > 0, scores.items()))
    return max(res, key=lambda x: x[1])[0] if len(res) > 0 else None


def read_auto_sep():
    success = False
    for sep in sep_symbols:
        try:
            df = pd.read_csv('soap.csv', sep=sep)
            if len(df.columns) < 2:
                raise ValueError("Skip")
        except:
            continue
        else:
            success = True
            break
    if success:
        return df
    else:
        raise ValueError("Can't detect separator")


def get_chart_data(df: pd.DataFrame):
    chart_data = {}
    df = df.drop_duplicates()
    max_rows = 1000
    if df.shape[0] > max_rows:
        df = df.sample(max_rows)
    for column, _type in zip(df.columns, df.dtypes):
        if _type == 'int':
            chart_data[column] = {'type': 'line', 'data': df[column]}
        elif _type == 'object':
            sep = get_separator(df[column])
            is_cat = check_categories(df[column])
            if is_cat and not sep:
                chart_data[column] = {'type': 'pie', 'data': {
                    unique: amount / df.shape[0] for unique, amount in df[column].value_counts().items()
                }}

            if sep:
                chart_data[column] = {'type': 'bar', 'data': value_counts(df[column].str.split(sep)).to_dict()}
    return chart_data
