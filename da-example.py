# %% Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

import matplotlib.axes._axes as axes
import matplotlib.figure as figure
import sqlite3

plt.style.use('ggplot')

# %% Conexión a base de datos
conn = sqlite3.connect("./data_db/Chinook_Sqlite.sqlite")

# %% Ejemplo de query y obtención

df = pd.read_sql_query("SELECT * from Invoice", conn)
g_country = df.groupby(['BillingCountry'])[['BillingCountry']].agg('count')
