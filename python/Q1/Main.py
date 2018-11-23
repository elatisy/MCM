import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as axes3d
import numpy as np
import xlrd
import xlwt

import python.Q1.line_chart as lc
import python.Q1.histogram_3d as h3d
import python.Q1.export_demands_xls as edx


def str_to_int(string):
    try:
        return int(string)
    except Exception as e:
        return ''


files = {
    '2015': ['09', '10', '11', '12'],
    '2016': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2017': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2018': ['01', '02', '03', '04', '05', '06', '07', '08']
}

data = {}
sectors = []
x = []
y = []
x_counter = 1
y_counter = 1
for year in files:
    for month in files[year]:
        y.append(y_counter)
        y_counter += 1

        file_name = '../data/' + year + '/' + month + '.xlsx'

        xlsx = xlrd.open_workbook(file_name)
        table = xlsx.sheets()[0]

        nrows = table.nrows - 1
        ncols = table.ncols

        data_temp = {}
        for i in range(3, nrows):
            sector = table.row(i)[1].value
            data_temp[sector] = str_to_int(table.row(i)[2].value)
            if sector not in sectors:
                sectors.append(sector)
                x.append(x_counter)
                x_counter += 1
        data[year + month] = data_temp


"""
Export a xls that contents the total demands of every sector in 36 sheets
"""
# edx.export_demands(data, sectors)

"""
draw some line chart with given data
"""
# lc.draw_line_chart(data, 'Sales management', 'Total demands of sales management')

"""
draw the 3D-histogram graph about demands of five categories
"""
h3d.draw_histogram_3d()
