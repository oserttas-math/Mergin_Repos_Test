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
sales.groupby('city')[['bread', 'butter']].agg(['max', 'sum'])

def drange(series):
    return series.max() - series.min()


# Aggregation with custom functions
sales.groupby('weekday')[['bread', 'butter']].agg(drange)

# Aggregation with dictionary
sales.groupby('weekday')[['bread', 'butter']].agg({'bread': 'sum', 'butter': drange})

sales.groupby(Customers)[['bread', 'butter']].agg({'bread': 'sum', 'butter': drange})


def zscore(series):
    return (series - series.mean()) / series.mean()


# Transform the Bread data to z-score values
zscore(sales['bread']).head()
