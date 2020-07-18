import numpy as np
import pandas
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer

# handle the missing values
data = pandas.DataFrame([[4.0, 45.0, 984.0], [np.NAN, np.NAN, 5.0], [94.0, 23.0, 55.0]])

# print original data
print(data)

# fill the missing values with the constant 0.1
print(data.fillna(0.1))

# fill the missing values with the mean
print(data.fillna(data.mean()))

# Data normalization

data1 = pandas.DataFrame([[58.0, 1.0, 43.0], [10.0, 200.0, 65.0], [20.0, 75.0, 7.0]])

# scaling with min-max scaler
scaled_values = MinMaxScaler(feature_range=(0, 1))
results = scaled_values.fit(data1).transform(data1)
print(results)

# scaling with the standard scaling
stand_scalar = StandardScaler().fit(data1)
results = stand_scalar.transform(data1)
print(results)

# normalization using binarization
results = Binarizer(50.0).fit(data1).transform(data1)
print(results)
