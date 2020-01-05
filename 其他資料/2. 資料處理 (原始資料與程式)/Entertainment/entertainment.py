
# 引用套件
import pickle
import csv
import pandas as pd

#################################################################################

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分7個欄位，分別為：縣市名、地區名等等
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key,key_1,0,0,0,0,0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名','地區名','電影院', 
                                                '百貨','好市多','全聯','頂好']) 

#################################################################################

# 讀取電影院數據
file = open('電影院.csv', 'r')  # 讀取醫療資源csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
cinema_col = []

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

#
for col in row:
    cinema_col.append(col[3].replace("\n",""))

#################################################################################

# 讀取購物中心數據
file = open('購物中心.csv', 'r')  # 讀取購物中心csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
mall_col = []

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    mall_col.append(col[3].replace("\n",""))

#################################################################################

# 讀取超市數據
file = open('超市家數.csv', 'r')  # 讀取超市家數csv檔
lines = file.readlines()         # 將csv檔的資料讀到lines
file.close()                     # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
cos_col = []
din_col = []
lian_col = []

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    cos_col.append(col[3])
    din_col.append(col[4])
    lian_col.append(col[5].replace("\n",""))

#################################################################################

for i in range(len(df.iloc[:,1])):
    df.iloc[i, 2] = cinema_col[i]
    df.iloc[i, 3] = mall_col[i]
    df.iloc[i, 4] = cos_col[i]
    df.iloc[i, 5] = din_col[i]
    df.iloc[i, 6] = lian_col[i]

# df.to_csv(path_or_buf = '/Users/wangyuda/Desktop/project/Entertainment/娛樂.csv')

