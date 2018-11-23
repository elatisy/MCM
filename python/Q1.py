import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D as axes3d
# import numpy as np
import xlrd

files = {
    '2015': ['09', '10', '11', '12'],
    '2016': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2017': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2018': ['01', '02', '03', '04', '05', '06', '07', '08']
}

data = {}
for year in files:
    for month in files[year]:
        file_name = '../data/' + year + '/' + month + '.xlsx'

        xlsx = xlrd.open_workbook(file_name)
        table = xlsx.sheets()[0]

        nrows = table.nrows
        ncols = table.ncols

        data_temp = {}
        for i in range(3, nrows - 1):
            data_temp[table.row(i)[1].value] = table.row(i)[2].value
            # for j in range(, ncols - 1):
        data[year + month] = data_temp
        # row = table.row(4)
        # print(row[1].value)

# print(data)
x = []
y = []
for time in data:
    x.append(time[4:])
    y.append(data[time]['Sales management'])

# print(len(x))
# print(len(y))

plot.bar(range(len(y)), y, color = 'rgb', tick_label = x)
plot.show()
