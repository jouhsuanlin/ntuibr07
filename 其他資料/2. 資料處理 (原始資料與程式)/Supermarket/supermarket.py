
# 引用套件
import pickle
import csv
import pandas as pd

#################################################################################

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分5個欄位，分別為：縣市名、地區名、好市多家數、頂好家數、全聯家數
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key,key_1,0,0,0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名','地區名','好市多家數', 
                                                '頂好家數','全聯家數'])
                  


#################################################################################

city_list = ['臺北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','臺中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','臺南市','高雄市','澎湖縣','金門縣','屏東縣','臺東縣',
             '花蓮縣']

city_list_0 = ['台北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','台中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','台南市','高雄市','澎湖縣','金門縣','屏東縣','台東縣',
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
file = open('超市家數.csv', 'r')  # 讀取超市家數csv檔
lines = file.readlines()         # 將csv檔的資料讀到lines
file.close()                     # 關閉csv檔

row = []       # 定義列陣列，放入各行csv資料
city_col = []
area_col = []
cos_col = []
din_col = []
lian_col = []

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

row.pop(0)

# 
for col in row:
    city_col.append(col[1])
    area_col.append(col[2])
    cos_col.append(int(float(col[3])))
    din_col.append(int(float(col[4])))
    lian_col.append(int(float(col[5].replace("\n",""))))

#################################################################################

for i in range(len(df.iloc[:,1])):
    for j in range(len(area_col)):
        if df.iloc[i, 1] in area_col[j]:
            if city_list_0[city_list.index(df.iloc[i, 0])] in city_col[j]:
                df.iloc[i, 2] = cos_col[j]
                df.iloc[i, 3] = din_col[j]
                df.iloc[i, 4] = lian_col[j]

# df.to_csv(path_or_buf = '/Users/wangyuda/Desktop/project/Crime/犯罪率.csv')









