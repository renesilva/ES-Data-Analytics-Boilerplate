# %% Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gspread as gs
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

# %% Conexión a Google Spreadsheets
gc = gs.service_account(filename='credentials/')  # nombre de la llave
sh = gc.open_by_url('')  # URL
ws = sh.worksheet('')  # nombre del worksheet
df = pd.DataFrame(ws.get_all_records())
df.head()
