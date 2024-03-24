# libraries
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

df_2016 =pd.read_csv('properties_2016.csv')
df_train_2016 =pd.read_csv('train_2016_v2.csv', parse_dates=["transactiondate"])


# EDA - 2016
print(df_2016.shape)
display(df_2016.head())
