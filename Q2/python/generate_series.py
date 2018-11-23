import xlrd
import pandas as pd


def get_series(file = '../../Q1/data/demands(tagged).xls'):
    table = xlrd.open_workbook(file).sheets()[0]
    ncols = table.ncols

    series_index = []
    series_data = []
    for i in range(3, ncols):
        date = table.row(0)[i].value[:4] + '-' + table.row(0)[i].value[4:]
        series_index.append(date)
        series_data.append(table.row(2)[i].value)

    series_index = pd.to_datetime(series_index)
    series = pd.Series(series_data, series_index)
    return series
