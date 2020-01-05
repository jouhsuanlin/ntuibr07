
# 將不同縣市的Excel檔案合併成一份csv檔

import pandas as pd

df_final = pd.read_excel('Medical.xlsx', sheet_name = 0)

def num_row(df):
    nrow_wanted = 1
    for i in range(df.iloc[:,0].size):
        if df.iloc[i,0] == '附註：1.97年起洗腎治療床名稱改為血液透析床。':
            nrow_wanted = i
            break
    return nrow_wanted

for i in range(1,23):
    file_name = str(i) + ".xls"

    df = pd.read_excel(file_name, skiprows = 7
        , sheet_name = 0)

    nrow_wanted = num_row(df)

    df = df.iloc[0:nrow_wanted, 0:5]

    df.columns =  ['區域別', '院所家數', '醫院家數', '診所家數', '醫療院所病床數']

    df_final = pd.concat([df_final, df], axis=0, ignore_index=True)

path = "/Users/wangyuda/Desktop/project/Medical/Final.csv"

df_final.to_csv(path_or_buf = path)

