import pandas as pd
import numpy as np
df_age = pd.DataFrame({'Name': ['Tom', 'Mike', 'Iverson', 'Ali', 'Mehmet'],
                      'Age': [60, 34, 45, 55, 10]
                       })
df_height = pd.DataFrame({'name': ['Tom', 'Mike', 'Iverson', 'Ali', 'Mehmet'],
                         'Height': [6.2, 4.0, 5.8, 6.6, 8.0]
                          })


# Join this two data frame on names:

joined = df_age.set_index('Name').join(df_height.set_index('name'))
print(joined)
