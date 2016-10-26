"""
Pandas introduction for Data Bootcamp course.

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/NYUDataBootcamp/Materials

Written by Chase Coleman, October 2016
Created with Python 3.5
"""

#%%
# We will always import pandas as pd -- This is more or less a
# convention across the data community
import pandas as pd

#%%
# This dictionary is similar to one that we saw earlier in the class
# It represents GDP/CPI data at 10 year intervals from 1990 to 2010
df = pd.DataFrame({"GDP": [5974.7, 10031.0, 14681.1],
                   "CPI": [127.5, 169.3, 217.488],
                   "Year": [1990, 2000, 2010],
                   "Country": ["US", "US", "US"]})
print(df)
print(type(df))

#%%

dft = df.T
print("\n", dft)

#%%
# This is for exercise!!!
data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA'],
        'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7],
        'rgdpe': [2.611, 4.951, 11.106, 1.294, 1.753, 2.032],
        'year': [1990, 2000, 2010, 1990, 2000, 2010]}
pwt = pd.DataFrame(data)

# Fill in your answers below

#%%

print(df["GDP"])
print(type(df["GDP"]))

#%%
print(df["GDP"] + df["GDP"])
print(df["GDP"] - df["GDP"])
print(df["GDP"] / df["CPI"])
print(df["CPI"] * df["CPI"])
print(df["GDP"] / 10000)

#%%
df['RGDP'] = df['GDP']/df['CPI']
df['GDP_div_1000'] = df['GDP'] / 1000

#%%

df.columns = ["cpi", "country", "gdp", "year", "rgdp", "gdp_div_1000"]

# Could also use
df.columns = [var.lower() for var in df.columns]
# or
df = df.rename(columns={"gdp": "ngdp"})

#%%
namelist = ['ngdp', 'rgdp']
numlist  = [2, 4]
df_v1 = df[namelist]
df_v2 = df[numlist]

#%%

df.drop(['cpi'], axis=1)

#%%

df = df.set_index(['year'])
df_reset = df.reset_index()

#%%
print(df.mean())
print(df.std())
print(df.describe())

#%%
df.plot()

