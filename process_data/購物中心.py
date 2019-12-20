# Mall

# 引用套件
import pickle
import csv
import pandas as pd

################################################################################

# 將縣市、地區、路名的對照資料轉為可使用的dictionary
# 並依各縣市、地區在dictionary的順序，建最後用來存資料的dataframe

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的dataframe，分3個欄位，分別為：縣市名、地區名、電影院家數
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key, key_1, 0])  # 縣市名、地區名、電影院家數(預設為0)

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名', '地區名', '購物中心家數'])

    # 記錄臺北市區域數，作為存入臺北市資料的區域尾數，之後用來記錄各縣市地區的資訊用，
    tail = len(road['臺北市'])

# 作為存入臺北市資料的區域首數
head = 0

################################################################################

# 各縣市清單
city_list = ['臺北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','臺中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','臺南市','高雄市','澎湖縣','金門縣','屏東縣','臺東縣',
             '花蓮縣']

# 各縣市清單，若資料中臺中市、臺北市等等的第一個字是「台」，則需使用這份清單來過濾
city_list_0 = ['台北市','基隆市','新北市','連江縣','宜蘭縣','新竹市','新竹縣',
             '桃園市','苗栗縣','台中市','彰化縣','南投縣','嘉義市','嘉義縣',
             '雲林縣','台南市','高雄市','澎湖縣','金門縣','屏東縣','台東縣',
             '花蓮縣']

"""
# 縣市對照編號
city_list = ['臺北市0','基隆市1','新北市2','連江縣3','宜蘭縣4',
             '新竹市5','新竹縣6','桃園市7','苗栗縣8','臺中市9',
             '彰化縣10','南投縣11','嘉義市12','嘉義縣13',
             '雲林縣14','臺南市15','高雄市16','澎湖縣17',
             '金門縣18','屏東縣19','台東縣20','花蓮縣21']
"""

################################################################################

# 從csv檔擷取需要過濾的地址資料

file = open('mall.csv', 'r')  # 讀取電影院資訊的csv檔
lines = file.readlines()      # 將csv檔的資料讀到lines
file.close()                  # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
address_col = []  # 定義欄陣列，放入第1欄的地址資訊

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

# 將第0欄與第5欄的城市名與地址資訊放入city_col與address_col
for col in row:
    address_col.append(col[1])


################################################################################
# 將所有地址整理到address_col大清單後，開始進行過濾與計算

# 依縣市序號逐一過濾
for city in range(22):
    # 由後往前過濾，若過濾成功就從address_col中刪除，之後可以成為debug的資訊來源
    for i in range(len(address_col) - 1, 0, -1):
        # 在某縣市的某幾區中
        for j in range(head, tail):
            # 濾網一：若城市名出現在地址中，則進入濾網二（資料中的城市名沒有出現「台」）
            # 若資料中的城市名只出現「台」，則濾網需改為city_list_0
            # 若資料中的城市名出現「台」、「臺」混用，則兩個濾網都需要使用
            if city_list[city] in address_col[i]:
                # 濾網二：若地區名出現在地址中
                if df.iloc[j, 1] in address_col[i]:
                    df.iloc[j, 2] += 1               # 計數器加一
                    address_col.pop(i)               # 從address_col中去除已過濾資料
                    break                            # 跳出迴圈，檢索下一個地址
 
    # 更新head與tail的資訊，由於宜蘭後面多一筆「釣魚台（縣市）、釣魚台（地區）」
    # 因此多了city == 3與city == 4的情形做調整
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





