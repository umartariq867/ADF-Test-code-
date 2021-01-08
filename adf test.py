# imported adfull from statsmodel library
from statsmodels.tsa.stattools import adfuller
import pandas as pd
df = pd.read_csv('daily-total-female-births.csv', header=0, index_col=0, squeeze=True)
# put all values in X variable
X = df.values
# app adfuller test on the data(x) and stored it in Result
result = adfuller(X)
print("printing of adf test all values:",result)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

if result[0]< result[4]["5%"]:
	print("Rejected Null Hypothesis - so the time series is non stationary")
	# print("Fail to reject null hypothesis - so time series in stationary")
else:
	print("Rejected Null Hypothesis - so the time series is non stationary")
	# # print("Fail to reject null hypothesis - so time series in stationary")