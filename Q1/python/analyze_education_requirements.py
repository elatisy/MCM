import xlwt

def analyze_education_requirements(data : dict):
    file = xlwt.Workbook()
    table = file.add_sheet('Sheet 1')

    headers = [
        'sectors',
        'At senior high school and below',
        'rate',
        'At bachelor-related degree',
        'rate',
        'At master and above',
        'rate',
        'Unlimited',
        'rate'
    ]

    j = 0
    for header in headers:
        table.write(0, j, header)
        j += 1

    i = 1
    for sector, requirements in data.items():
        table.write(i, 0, sector)

        total_requirements = sum(requirements.values())

        j = 1
        for value in requirements.values():
            table.write(i, j, value)
            table.write(i, j + 1, (value / total_requirements * 100))
            j += 2
        i += 1

    file.save('../data/education_requirements.xls')