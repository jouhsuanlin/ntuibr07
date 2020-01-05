
# 引用套件
import pickle
import csv
import pandas as pd

##############################################################################

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分3個欄位，分別為：縣市名、地區名、
    # 公車站牌數、地區土地面積(平方公里)、公車站牌密度(站/平方公里)
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key,key_1,0,0,0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名','地區名','公車站牌數', 
                      '地區土地面積(平方公里)','公車站牌密度(站/平方公里)',]) 

##############################################################################

# 讀取醫療資源數據
file = open('公車站牌數_Output.csv', 'r')  # 讀取公車站牌數csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
stop_col = []     # 定義欄陣列，放入站牌數資料

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    stop_col.append(int(col[3]))

##############################################################################

# 讀取區域人口數據
file = open('各鄉鎮市區_土地面積_人口數.csv', 'r')  # 讀取區域人口數csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
area_col = []  # 定義欄陣列，放入第5欄的地址資訊

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    area_col.append(float(col[3]))

##############################################################################

for i in range(len(df.iloc[:,1])):
    df.iloc[i, 2] = stop_col[i]
    df.iloc[i, 3] = area_col[i]
    df.iloc[i, 4] = round(stop_col[i] / area_col[i], 2)


# df.to_csv(path_or_buf = '/Users/wangyuda/Desktop/project/Crime/犯罪率.csv')

