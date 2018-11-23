import matplotlib.pyplot as plt
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

        data[year + month] = data_temp

x = []
y = []
for time in data:
    x.append(time[2:])
    y.append(data[time]['Sales management'])

plt.title('Total demand of sales management')
plt.plot(x, y)

plt.show()
