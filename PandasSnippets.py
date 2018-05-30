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


print(joind.groupby('Gender').apply(agg))
