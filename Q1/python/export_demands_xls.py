import xlwt


def export_demands(data, sectors):
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
