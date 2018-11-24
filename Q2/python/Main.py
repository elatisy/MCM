import numpy as np
import pandas as pd
from datetime import datetime

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import Q2.python.test_stationarity as test_stationarity
from Q2.python.generate_series import get_series
import matplotlib.pyplot as plt

ts = get_series()
ts_log = np.log(ts)
# test_stationarity.draw_ts(ts_log)
#
# test_stationarity.draw_trend(ts_log, 12)

diff_12 = ts_log.diff(1)
diff_12.dropna(inplace=True)
diff_12_1 = diff_12.diff(1)
diff_12_1.dropna(inplace=True)
test_stationarity.test_stationarity(diff_12_1)

decomposition = seasonal_decompose(ts_log, model="additive")

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
test_stationarity.test_stationarity(ts_diff_1)

ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)

# for x in ts:
#     print(x)

# temp = [x for x in ts]
# print(temp)
model = ARIMA(ts, order=(2, 0, 2)) #2 0 2

result_arma = model.fit()

predict_ts = result_arma.predict()
# 一阶差分还原
diff_shift_ts = ts_diff_1.shift(1)
diff_recover_1 = predict_ts.add(diff_shift_ts)
# 再次一阶差分还原
rol_shift_ts = rol_mean.shift(1)
diff_recover = diff_recover_1.add(rol_shift_ts)
diff_recover.dropna(inplace=True)
print(diff_recover)
# for x in diff_recover:
#     print(x)
# 移动平均还原
rol_sum = ts_log.rolling(window=11).sum()
rol_recover = diff_recover*12 - rol_sum.shift(1)
# 对数还原
log_recover = np.exp(rol_recover)
log_recover.dropna(inplace=True)

ts = ts[log_recover.index]  # 过滤没有预测的记录
plt.figure(facecolor='white')
log_recover.plot(color='blue', label='Predict')
ts.plot(color='red', label='Original')
plt.legend(loc='best')
plt.title('RMSE: %.4f'% np.sqrt(sum((log_recover-ts)**2)/ts.size))
plt.show()


# series = get_series()
# origin = np.log(series)
# # print(origin)
# # ts.draw_ts(origin)
# ts.draw_trend(origin, 12)


# series = series.diff(1)
# diff_1 = np.log(series)
# print(series)

# series = series.diff(1)
# diff_2 = np.log(series)
# print(series)
# print(ts.testStationarity(series['2015-11':]))

# ts.draw_trend(series, 12)
# series_index = []
# month = 1
# for month in range(11, 13):
#     series_index.append(str(2015) + '-' + str(month))
# for year in range(2016, 2021):
#     for month in range(1, 13):
#         series_index.append(str(year) + '-' + str(month))
# for month in range(1, 9):
#     series_index.append(str(2021) + '-' + str(month))
#
# series_index = pd.to_datetime(series_index)
#
# # series_index = ['2015-09', '2015-10', '2015-11', '2015-12',
# #                 '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12',
# #                 '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
# #                 '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08'
# #                 ]
#
# series_value = [-1591, 375, -574, 7076, 152, -12810, 5281, 274, 907, -274, 846, 3327, -7144, 2624, 549,
#                 13106, -20960, 6546, 240, 1329, 218, -24, 160, -409, -132, 951, -1450, 1944, 3597, -9698,
#                 5712, -1083, 434, -121, 604.3595675529835, -1617.078026063126, 1049.529473854595, 472.9186659890964,
#                 -1441.085491418591, 1805.839984571253, -1527.294837961326, 760.0838911003701, 167.861951048089,
#                 -938.950737372653, 1298.385865081104, -1185.957656093545, 680.6109587601771, -11.08475064004657,
#                 -591.6228884263692, 919.0140817317816, -905.9440295941749, 582.7580355574722, -107.3262863484491,
#                 -356.0667878843261, 639.5033437674558, -681.6383004994475, 482.7986685939753, -151.0230935865215,
#                 -199.9893263256367, 436.5445439265896, -505.5258374483446, 389.7209623311465, -162.737327467405,
#                 -99.51076347788322, 291.3615019466715, -369.6660676522033, 307.8434361607594, -156.1791878151555,
#                 -37.22746548682401, 189.1416028694111
# ]
#
# series = pd.Series(series_value, series_index)
#
# series = series.shift(1)
# series = series.shift(1)
#
# for value in series:
#     print(value)
# print(series[:'2018'])
# print(series['2019':])
# series_index = pd.to_datetime(series_index)
