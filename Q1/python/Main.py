import xlrd

import Q1.python.line_chart as lc
import Q1.python.histogram_3d as h3d
import Q1.python.export_demands_xls as edx
import Q1.python.analyze_education_requirements as aer


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

education_requirements = {}
education_degrees = {
    'At senior high school and below'   : range(3, 6),
    'At bachelor-related degree'        : range(6, 8),
    'At master and above'               : range(8, 11),
    'Unlimited'                         : range(11, 12)
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

        file_name = '../../data/' + year + '/' + month + '.xlsx'

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

                education_requirements[sector] = {}
                for degree in education_degrees:
                    education_requirements[sector][degree] = 0

            for degree, __range in education_degrees.items():
                temp = 0
                for j in __range:
                    requirement = str_to_int(table.row(i)[j].value)
                    if requirement is not '':
                        temp += requirement

                education_requirements[sector][degree] += temp

        data[year + month] = data_temp

"""
Generate the analysis of the education requirements of the sectors
"""
aer.analyze_education_requirements(education_requirements)

"""
Export a xls that contents the total demands of every sector in 36 sheets
"""
edx.export_demands(data, sectors)

"""
draw some line chart with given data
"""
lc.draw_line_chart(data, 'Sales management', 'Total demands of sales management')

"""
draw the 3D-histogram graph about demands of five categories
"""
h3d.draw_histogram_3d()
