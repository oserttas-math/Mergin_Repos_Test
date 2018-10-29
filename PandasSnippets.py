import pandas as pd
import numpy as np

# JOIN TWO DF #

df_age = pd.DataFrame({'Name': ['Aomm', 'Jenny', 'Iverson', 'Ali', 'Ayse'],
                      'Age': [18, 34, 45, 55, 39]
                       })
df_height = pd.DataFrame({'Name': ['Aomm', 'Jenny', 'Iverson', 'Ali', 'Ayse'],
                         'Height': [5.2, 4.0, 5.8, 6.6, 5.0]
                          })


# Join those two data frame on names:

joined = df_age.set_index('Name').join(df_height.set_index('Name'))
print(joined)

########################################################

# CUSTOM AGG FUNCTION #

def agg(dfs):
    '''Returns STD and Mean of Gender Groups and
       Ranked Name, Height and Age Data Within Gorups'''
    data = {'Name': max(dfs['Name']),
            'Oldest': max(dfs['Age']),
            'Std-Height': dfs['Height'].std(),
            'Mean-Height': dfs['Height'].mean()
            }

    new_df = pd.Series(data)
    return new_df


joind = joined.reset_index()
joind['Gender'] = pd.Series(['Male', 'Female', 'Male', 'Male', 'Female'])
print(joind)

# Result :
print(joind.groupby('Gender').apply(agg))

#######################################################
# Groupby : Split-Apply-Combine
# df.groupby('split').apply()
# You could choose columns of interest by edding ['colunm_name'] after groupby
# method

# Groupby Example

import pandas as pd
sales = pd.DataFrame(
                     {
                       'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
                       'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
                       'bread': [139, 237, 326, 456],
                       'butter': [20, 45, 70, 98]
                     }
                    )

# Problem : Find number of sales on Sunday

sales.loc[sales['weekday'] == 'Sun'].count()

# Alternative way: sales on each day

sales.groupby('weekday').count()


# Total bread sales each day

sales.groupby('weekday')['bread'].sum()

sales.groupby('weekday')[['bread', 'butter']].sum()


# Multi-Level splitting

sales.groupby(['city', 'weekday']).mean()

sales.groupby(['city', 'weekday']).std()


# Now create a series with the same indexes with sales dataframe then observe

Customers = pd.Series(['Ali', 'Raji', 'Liz', 'Robert'])
sales.groupby(Customers)['bread'].sum()
# Also, two dataframe with the same index values satisfy above nesting process
# Result: New series with the customer names on the index


# Now aggregations

sales.groupby('city')[['bread', 'butter']].max()


# Multiple aggregations

aggregated = sales.groupby('city')[['bread', 'butter']].agg(['max', 'sum'])

# Retrun max values of selected column/columns

print(aggregated.loc[:, ('bread', 'max')])
print(aggregated.loc[:, (['bread', 'butter'], 'max')])
def drange(series):
    return series.max() - series.min()

# Aggregation with custom functions

sales.groupby('weekday')[['bread', 'butter']].agg(drange)

# Aggregation with dictionary
sales.groupby('weekday')[['bread', 'butter']].agg({'bread': 'sum', 'butter': drange})

sales.groupby(Customers)[['bread', 'butter']].agg({'bread': 'sum', 'butter': drange})


# Transforming datetime to days of the week

ds = pd.DataFrame(
             {'time': ['2015-02-02 08:30:00', '2015-02-02 21:00:00',
              '2015-02-03 14:00:00', '2015-02-04 15:30:00',
              '2015-02-04 22:00:00', '2015-02-05 02:00:00',
              '2015-02-05 22:00:00', '2015-02-07 23:00:00',
              '2015-02-09 09:00:00', '2015-02-09 13:00:00'],
              'sales': [4, 6, 20, 9, 2, 3, 20, 30, 2, 8]

             }
)

ds['time'] = pd.to_datetime(ds['time'])
print(ds.set_index('time',inplace=True))
print(ds.index.strftime('%a'))
# >>> output : ['Mon' 'Mon' 'Tue' 'Wed' 'Wed' 'Thu' 'Thu' 'Sat' 'Mon' 'Mon']

# Transform method with z-normalization

def zscore(series):
    return (series - series.mean()) / series.mean()


# Transform the Bread data to z-score values
zscore(sales['bread']).head()
