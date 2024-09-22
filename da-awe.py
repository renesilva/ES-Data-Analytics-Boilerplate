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

# %% Read base file
df = pd.read_csv('data_in/csv-zulema.csv')
df['ciudad'] = df['AJUSTE CIUDAD']

# %% Fix descripcion
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE-TARIJA', 'AWE TARIJA')
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE, COBIJA', 'AWE COBIJA')
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE, ENCUENTRO', 'AWE ENCUENTRO')
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE HONORARIOS', 'AWE BOLIVIA')
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE ACTIVIDAD BOLIVIANA', 'AWE BOLIVIA')
df['DescripTransacción'] = df['DescripTransacción'].str.replace('AWE NETBITS PREMIO', 'PREMIO SEMILLA')

# %% change cities
cities = [
    'AWE SANTA CRUZ',
    'AWE COCHABAMBA',
    'AWE LA PAZ',
    'AWE TARIJA',
    'AWE COBIJA',
    'AWE ORURO',
    'AWE SUCRE',
    'AWE ENCUENTRO',
    'AWE BOLIVIA',
    'PREMIO SEMILLA',
]
for city in cities:
    cond = df['DescripTransacción'].str.contains(city)
    df.loc[cond, 'ciudad'] = city

# %% group and sum by 'desc'
g_by_desc_ciudad = df.groupby(['ciudad'])[['DebeBs']].agg('sum')

# %% split column by delimiter
df['programa'] = df['DescripTransacción'].str.split('-').str[-1]

# %% fix programas text
df['programa'] = df['programa'].str.replace(',', '')
df['programa'] = df['programa'].str.replace(' OPERATIVOS', '')
df['programa'] = df['programa'].str.replace(' OPERATIVO', '')
df['programa'] = df['programa'].str.replace(' VARIOS', '')
df['programa'] = df['programa'].str.replace(' EJECUCION', '')
df['programa'] = df['programa'].str.replace(' EVENTOS', '')
df['programa'] = df['programa'].str.replace(' S/FAC', '')
df['programa'] = df['programa'].str.replace(' S/F', '')
df['programa'] = df['programa'].str.replace('2023', '')
df['programa'] = df['programa'].str.replace('2022', '')
df['programa'] = df['programa'].str.replace('22', '')
df['programa'] = df['programa'].str.replace('23', '')
df['programa'] = df['programa'].str.replace('CAMPAÑAS', 'AWE BOLIVIA')
df['programa'] = df['programa'].str.strip()

# %% group and sum by 'desc'
g_by_desc = df.groupby(['programa'])[['DebeBs']].agg('sum')
