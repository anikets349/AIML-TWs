import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

boston = load_boston()
print(boston)

df_x = pd.DataFrame(boston.data, columns = boston.feature_names)
df_y = pd.DataFrame(boston.target)

# generate descriptive statistics
print(df_x.describe())
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.33, random_state = 42)
# fit a linear model
reg.fit(x_train, y_train)
print(reg.coef_)
y_pred = reg.predict(x_test)
print(y_pred)
y_pred[2]
y_test[0]

print(np.mean(y_pred - y_test) ** 2)
print(mean_squared_error(y_test, y_pred))
