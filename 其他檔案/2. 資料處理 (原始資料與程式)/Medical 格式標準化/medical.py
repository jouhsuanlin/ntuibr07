
# 引用套件
import pickle
import csv
import pandas as pd

#################################################################################

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分10個欄位，分別為：縣市名、地區名等等
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key,key_1,0,0,0,0,0,0,0,0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名','地區名','院所家數','人均院所家數(家數/千人)',
                                                '診所家數','人均診所家數(家數/千人)','醫療院所病床數',
                                                '人均病床數(床數/千人)','大醫院家數','地區人口數'])

#################################################################################

city_list = ['臺北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','臺中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','臺南市','高雄市','澎湖縣','金門縣','屏東縣','臺東縣',
             '花蓮縣']

''' 
# 縣市對照編號
city_list = ['臺北市0','基隆市1','新北市2','連江縣3','宜蘭縣4',
             '新竹市5','新竹縣6','桃園市7','苗栗縣8','臺中市9',
             '彰化縣10','南投縣11','嘉義市12','嘉義縣13',
             '雲林縣14','臺南市15','高雄市16','澎湖縣17',
             '金門縣18','屏東縣19','台東縣20','花蓮縣21']
'''
#################################################################################

# 讀取醫療資源數據
file = open('醫療資源.csv', 'r')  # 讀取醫療資源csv檔
lines = file.readlines()         # 將csv檔的資料讀到lines
file.close()                     # 關閉csv檔

row = []       # 定義列陣列，放入各行csv資料
Area_col = []  # 定義欄陣列
Cli_Hos_col = []
Cli_col = []
Hos_col = []
Bed_col = []

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    Area_col.append(col[1])
    Cli_Hos_col.append(int(float(col[2])))
    Hos_col.append(int(float(col[3])))
    Cli_col.append(int(float(col[4])))
    Bed_col.append(int(float(col[5])))

#################################################################################

# 讀取區域面積數據
file = open('各鄉鎮市區_土地面積_人口數.csv', 'r')  # 讀取區域人口資源csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []      # 定義列陣列，放入各行csv資料
Pop_col = []  # 定義欄陣列，放入第5欄的地址資訊

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    Pop_col.append(int(float(col[2])))

#################################################################################

for i in range(len(df.iloc[:,1])):
    df.iloc[i, 9] = int(Pop_col[i])

for i in range(len(df.iloc[:,1])):
    for j in range(len(Area_col) - 1, 0, -1):
        if df.iloc[i, 1] in Area_col[j]:
            if df.iloc[i, 0] in Area_col[j]:
                df.iloc[i, 2] = int(float(Cli_Hos_col[j]))
                df.iloc[i, 4] = int(float(Cli_col[j]))
                df.iloc[i, 6] = int(float(Bed_col[j]))
                df.iloc[i, 8] = int(float(Hos_col[j]))

                df.iloc[i, 3] = round(float(Cli_Hos_col[j]) / df.iloc[i, 9] * 1000, 3)
                df.iloc[i, 5] = round(float(Cli_col[j]) / df.iloc[i, 9] * 1000, 3)
                df.iloc[i, 7] = round(float(Bed_col[j]) / df.iloc[i, 9] * 1000, 3)
                break
            else:
                continue
        else:
            continue

# df.to_csv(path_or_buf = '/Users/wangyuda/Desktop/project/Medical2/醫療資源.csv')

