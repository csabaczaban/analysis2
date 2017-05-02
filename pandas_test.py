__author__ = 'Gergely'

import pandas as pd
import statsmodels as sm

dataframe = pd.read_excel(r'correlation.xlsx', header=None, names=[['column_1', 'column_2']])

# print(dataframe)

target = dataframe['column_1']
training = dataframe['column_2']

# initiating model
model = sm.Logit(target, training)

# fitting model
model.fit()
parameters = model.parameters()

# predicting with unseen data
model.predict(parameters, unseen_data)
