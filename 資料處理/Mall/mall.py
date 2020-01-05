# Mall

# 引用套件
import pickle
import csv
import pandas as pd

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分3個欄位，分別為：縣市名、地區名、購物中心家數
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key, key_1, 0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名', '地區名', '購物中心家數'])

    # 記錄臺北市區域數，作為存入臺北市資料的區域尾數，之後用來記錄各縣市地區的資訊用，
    tail = len(road['臺北市'])

# 作為存入臺北市資料的區域首數
head = 0


city_list = ['臺北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','臺中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','臺南市','高雄市','澎湖縣','金門縣','屏東縣','臺東縣',
             '花蓮縣']

file = open('mall.csv', 'r')  # 讀取購物中心資訊的csv檔
lines = file.readlines()      # 將csv檔的資料讀到lines
file.close()                  # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
address_col = []  # 定義欄陣列，放入第1欄的地址資訊

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

# 將地址資訊放入address_col
for col in row:
    address_col.append(col[1])

for city in range(22):
    for i in range(len(address_col) - 1, 0, -1):
        for j in range(head, tail):
            if city_list[city] in address_col[i]:
                if df.iloc[j, 1] in address_col[i]:
                    df.iloc[j, 2] += 1
                    address_col.pop(i)
                    break
    if city != 21:
        if city == 3:
            head += len(road[city_list[city]])
            tail += len(road[city_list[city + 1]]) + 1
        elif city == 4:
            head += len(road[city_list[city]]) + 1
            tail += len(road[city_list[city + 1]])
        else:
            head += len(road[city_list[city]])
            tail += len(road[city_list[city + 1]])





