import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def draw_trend(series, size):
    rol_mean = series.rolling(window=size).mean()

    data_frame = pd.DataFrame(series)
    rol_weighted_mean = data_frame.ewm(span = size).mean()

    rol_weighted_mean.plot(color='black', label='Weighted Rolling Mean')
    series.plot(color='blue', label='Original')
    rol_mean.plot(color='red', label='Rolling Mean')
    plt.legend(loc='best')
    plt.title('Rolling Mean')
    plt.show()


def draw_ts(series):
    fig = plt.figure()
    series.plot(color='blue')
    plt.show()


def test_stationarity(ts):
    df_test = adfuller(ts)
    df_output = pd.Series(df_test[0:4], index=[
        'Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'
    ])
    for key, value in df_test[4].items():
        df_output['Critical Value (%s)' % key] = value
    return df_output


def draw_acf_pacf(ts, lags = 2):
    fig = plt.figure(facecolor='white')
    ax1 = fig.add_subplot(211)
    plot_acf(ts, lags=lags, ax=ax1)
    ax2 = fig.add_subplot(212)
    plot_pacf(ts, lags=lags, ax=ax2)
    plt.show()
