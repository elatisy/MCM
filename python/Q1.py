import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as axes3d
import numpy as np
import xlrd
import xlwt


def str_to_int(string):
    try:
        return int(string)
    except Exception as e:
        # print(sector)
        # print(__year + __month + __sector)
        return ''


files = {
    '2015': ['09', '10', '11', '12'],
    '2016': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2017': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    '2018': ['01', '02', '03', '04', '05', '06', '07', '08']
}

data = {}
sectors = []
for year in files:
    for month in files[year]:
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
        data[year + month] = data_temp

file = xlwt.Workbook()
table = file.add_sheet('Sheet 1')

table.write(0, 0, '职位/demand/时间')

i = 1
for sector in sectors:
    table.write(i, 0, sector)
    i += 1

j = 0
for time in data:
    j += 1
    i = 1
    table.write(0, j, time)
    for sector in sectors:
        if sector in data[time]:
            table.write(i, j, data[time][sector])
        else:
            table.write(i, j, '')
        i += 1

file.save('../data/demands.xls')

# figure1 = plt.figure()
# # figure2 = plt.figure()
#
# axes = axes3d(figure1)
#
# x = []
# xlsx = xlrd.open_workbook('../data/2016/04.xlsx')
# table = xlsx.sheets()[0]
# nrows = table.nrows - 1
# for i in range(3, nrows - 1):
#     x.append(table.row(i)[1].value)
#
# ncols = table.ncols
#
# y = []
# z = []
# for time in data:
#     y.append(time[2:])
#     temp = []
#     for sector in data[time]:
#         if time < '201704':
#             temp.append(0)
#         temp.append(data[time][sector])
#     # print(np.array(temp))
#     # z.append(temp)

# z = np.array(z)
#
# print(z)
#
# axes.plot_surface(x, y, z, cstride=1, rstride=1, cmap=plt.cm.coolwarm)
#
# plt.show()

# x = []
# y = []
# for time in data:
#     x.append(time[2:])
#     y.append(data[time]['Sales management'])
#
# plt.title('Total demand of sales management')
# plt.plot(x, y)
#
# plt.show()

