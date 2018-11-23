import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as axes3d
import numpy as np
import xlrd


def import_demands():
    xls = xlrd.open_workbook('../../data/Q1/demands(tagged).xls')
    table = xls.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols

    times = {}
    for i in range(3, ncols):
        times[i - 3] = table.row(0)[i].value

    categories = {}
    for i in range(1, nrows):
        category = table.row(i)[0].value

        if category not in categories:
            temp = {}
            for time in times:
                temp[times[time]] = 0
            categories[category] = temp

        for j in range(3, ncols):
            demand = table.row(i)[j].value
            if demand is '':
                demand = 0
            categories[category][times[j - 3]] += demand

    return {'categories': categories, 'times': times}


def draw_histogram_3d():
    colors = ['b', 'c', 'm', 'pink', 'r', 'b']
    counter = 1
    y_max = 36

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    data = import_demands()
    categories = data['categories']
    legend = {}

    categories_name = ['Human Resource', 'Others', 'Science and Technology', 'Community Service', 'Finance and Economic']

    for category in categories_name:

        y = []
        x = []
        for i in range(0, y_max):
            y.append(counter)
            x.append((i + 1) * 0.2)

        z = []
        i = 0
        for time in categories[category]:

            z.append(categories[category][time])
            i += 1

        y = np.array(y)
        x = np.array(x)
        z = np.array(z)
        dx = 0.1 * np.ones_like(y)
        dy = 0.1 * np.ones_like(x)
        dz = z.copy()
        z = np.zeros_like(z)

        color = colors[counter - 1]
        ax.bar3d(x, y, z, dx, dy, dz, color=color, zsort='average', alpha=0.05)
        proxy = plt.Rectangle((0, 0), 1, 1, fc=color)
        legend[category] = proxy

        # if category == 'Others':
        #     break

        counter += 1

    proxys = []
    names = []
    for category in legend:
        names.append(category)
        proxys.append(legend[category])

    ax.set_xlabel('Time')
    ax.set_ylabel('Categories')
    ax.set_zlabel('Total Demands')
    plt.title('The bar chart of the change about total demands in five career categories', fontsize=20,
              verticalalignment='bottom')

    ax.legend(proxys, names)

    plt.show()


if __name__ == '__main__':
    draw_histogram_3d()
