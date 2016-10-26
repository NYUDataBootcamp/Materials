"""
Data input with Pandas for Data Bootcamp course.

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/NYUDataBootcamp/Materials

Written by Dave Backus, August 2015
Created with Python 3.4

Edited by Chase Coleman and Spencer Lyon, October 2016
Created with Python 3.5
"""

#%%
"""
Read csv file from internet (and why we like csv's)
The result is a data frame:  like a sheet with row and column labels
"""
import pandas as pd

# read file from url
url1 = 'https://raw.githubusercontent.com/NYUDataBootcamp'
url2 = '/Materials/master/Data/test.csv'
url  = url1 + url2
df = pd.read_csv(url)

# if the internet is down
#df_fromdict = pd.DataFrame({'name': ['Dave', 'Chase', 'Spencer'],
#            'x1': [1, 4, 5], 'x2': [2, 3, 6], 'x3': [3.5, 4.3, 7.8]})


#%%

# windows users only
# folder = "\C:\Users"  # WILL NOT WORK
folder = "\\C:\\Users"  # Good
folder = "/C:/Users"  # Good


# NEED TO CHANGE TO YOUR OWN PATH HERE
folder = "/Users/sglyon/Teaching/NYUDataBootcamp/Materials/Data/"
csv_file = folder + "test.csv"
df = pd.read_csv(csv_file)


#%%
"""
Examples
"""
import pandas as pd

# Penn World Table
url = 'http://www.rug.nl/research/ggdc/data/pwt/v81/pwt81.xlsx'
pwt = pd.read_excel(url, sheetname='Data')

#%%
# World Economic Outlook
url1 = 'https://www.imf.org/external/pubs/ft/weo/'
url2 = '2015/02/weodata/WEOOct2015all.xls'
weo = pd.read_csv(url1+url2,
                  sep='\t',                 # \t = tab
                  thousands=',',            # kill commas
                  na_values=['n/a', '--'])  # missing values

#%%
# PISA test scores
url = 'http://dx.doi.org/10.1787/888932937035'
pisa = pd.read_excel(url,
                     skiprows=18,       # skip the first 18 rows
                     skipfooter=7,      # skip the last 7
                     parse_cols=[0,1,9,13],   # select columns of interest
                     index_col=0,       # set the index as the first column
                     header=[0,1]       # set the variable names
                     )


#%%
pisa = pisa.dropna()                            # drop blank lines
pisa.columns = ['Math', 'Reading', 'Science']   # simplify variable names
pisa['Math'].plot(kind='barh', figsize=(5, 12))

#%%
# UN population data
url1 = 'http://esa.un.org/unpd/wpp/DVD/Files/'
url2 = '1_Indicators%20(Standard)/EXCEL_FILES/1_Population/'
url3 = 'WPP2015_POP_F07_1_POPULATION_BY_AGE_BOTH_SEXES.XLS'
url = url1 + url2 + url3

cols = [2, 4, 5] + list(range(6,28))
est = pd.read_excel(url, sheetname=0, skiprows=16, parse_cols=cols)

#%%
# income by colleage major
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2
df538 = pd.read_csv(url)
df538 = df538.set_index("Major")
df538["Median"].plot(kind="barh", figsize=(5, 12))

#%%
# IMDb movies and parts
# WARNING: this file is approx 200 MB -- this might take a while
url  = 'http://pages.stern.nyu.edu/~dbackus/Data/cast.csv'
cast = pd.read_csv(url, encoding='utf-8')

#%% first 2016 presdidential debate
# NOTE: data came from here:
# https://www.kaggle.com/mrisdal/2016-us-presidential-debates
url1 = "https://raw.githubusercontent.com/NYUDataBootcamp/Materials/"
url2 = "master/Data/pres_debate_2016.csv"
url= url1 + url2
debate = pd.read_csv(url)

# who spoke more
trump = debate[debate["Speaker"] == "Trump"]
clinton = debate[debate["Speaker"] == "Clinton"]

print("Length of Trumps's talking ", len(trump["Text"].sum()))
print("Length of Clinton's talking ", len(clinton["Text"].sum()))

#%%
"""
APIs
"""
from pandas_datareader import data  # Package to access FRED
import datetime as dt               # package to handle dates

start = dt.datetime(2010, 1, 1)  # start date
codes = ['GDPC1', 'PCECC96']     # real GDP, real consumption
fred  = data.DataReader(codes, 'fred', start)
fred = fred/1000                # convert billions to trillions

fred.plot()

#%%
# World Bank
from pandas_datareader import wb   # World Bank api

var = ['NY.GDP.PCAP.PP.KD']         # GDP per capita
iso = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']  # country codes
year = 2013
wbdf = wb.download(indicator=var, country=iso, start=year, end=year)

#%%
wbdf = wbdf.reset_index(level='year', drop=True)
wbdf.plot(kind='barh')

#%%
# Fama-French equity returns
from pandas_datareader import data  # Package to access FF

ff = data.DataReader('F-F_Research_Data_factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']      # rename variables

#%%
"""
Review
"""
data = {'EG.ELC.ACCS.ZS': [53.2, 47.3, 85.4, 22.1],    # access to elec (%)
        'IT.CEL.SETS.P2': [153.8, 95.0, 130.6, 74.8],  # cell contracts per 100
        'IT.NET.USER.P2': [11.5, 12.9, 41.0, 13.5],    # internet access (%)
        'Country': ['Botswana', 'Namibia', 'South Africa', 'Zambia']}
af = pd.DataFrame(data)

