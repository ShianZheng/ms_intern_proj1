import pandas as pd
import numpy as np


def dum_ori(row):   # the function to add dummy var to order_reason_id
    if row['ORDER_REASON_ID'] == 'CRR':
        return 1
    return 0


data = pd.read_csv('CU_QUALITY_DATA.txt', low_memory=False, dtype={'ORIGINAL_ORDER': str})

sLength = len(data['ORIGINAL_ORDER'])
data.loc[:, 'dum_ORDER_REASON_ID'] = pd.Series(np.random.randn(sLength), index=data.index)
data['ORDER_REASON_ID'] = data['ORDER_REASON_ID'].astype(str)
data['dum_ORDER_REASON_ID'] = data['dum_ORDER_REASON_ID'].astype(int)

data['dum_ORDER_REASON_ID'] = data.apply(lambda row: dum_ori(row), axis=1)  # add dummy var to CRR/non-CRR

print(data['dum_ORDER_REASON_ID'])
print(data['dum_ORDER_REASON_ID'].sum())

data.sort_values(by='ORIGINAL_ORDER')
df_no_na = data.dropna(subset=['ORIGINAL_ORDER'])       # drop all rows with NaN in 'ORIGINAL_ORDER'
df_no_na = df_no_na.sort_values(by='ORIGINAL_ORDER')    # sort the data

df_test = df_no_na.iloc[1:10000, ]  # first 10000 rows for testing
k = 1                               # set the default value of k to 1
df_test['rank'] = 1                 # add a new column 'rank' with default value 1

for i in range(1, len(df_test)):    # add row_number value to the column 'rank'
    if df_test.iloc[i, 1] == df_test.iloc[i-1, 1]:
        df_test.iloc[i, 27] = k
    else:
        k = k + 1
        df_test.iloc[i, 27] = k

temp = pd.DataFrame()    # create a temporary df for the next loop
for i in range(1, df_test.iloc[len(df_test)-1, 27]):
    

