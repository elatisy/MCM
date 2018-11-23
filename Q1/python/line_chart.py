import matplotlib.pyplot as plt


def draw_line_chart(data, sector, title):
    x = []
    y = []
    for time in data:
        x.append(time[2:])
        y.append(data[time][sector])

    plt.title(title)
    plt.plot(x, y)

    plt.show()
