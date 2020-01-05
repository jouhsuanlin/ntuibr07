# 最終版本

# 引用套件
import pickle
import csv
import pandas as pd

# 設定段數清單
section_num_1 = ['1段','2段','3段','4段','5段','6段','7段','8段','9段','3路']
section_num_2 = ['１段','２段','３段','４段','５段','６段','７段','８段','９段','３路']
section_chi = ['一段','二段','三段','四段','五段','六段','七段','八段','九段','三路']

#################################################################################

# 引入路名地區的pkl字典
with open('city_area_road.pkl', 'rb') as file:
    road = pickle.load(file)

    # 製作最後存資料的datafram，分3個欄位，分別為：縣市名、地區名、電影院家數
    # 先製作多列清單
    row_name = []
    for key in road:
        for key_1 in road[key]:
            row_name.append([key, key_1, 0])

    # 將清單轉為datafram的形式
    df = pd.DataFrame(data = row_name, columns=['縣市名', '地區名', '電影院家數'])

    # 記錄臺北市區域數，作為存入臺北市資料的區域尾數，之後用來記錄各縣市地區的資訊用，
    tail = len(road['臺北市'])

# 作為存入臺北市資料的區域首數
head = 0

#################################################################################

# 建立各縣市的名稱清單
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

file = open('2018_cinema_loc.csv', 'r')  # 讀取電影院資訊的csv檔
lines = file.readlines()                 # 將csv檔的資料讀到lines
file.close()                             # 關閉csv檔

row = []          # 定義列陣列，放入各行csv資料
city_col = []     # 定義欄陣列，放入第0欄的縣市資訊
address_col = []  # 定義欄陣列，放入第5欄的地址資訊

# 將csv各行資料放到row清單
for line in lines:
    row.append(line.split(','))

# 將第0欄與第5欄的城市名與地址資訊放入city_col與address_col
for col in row:
    city_col.append(col[0])
    address_col.append(col[5])

# 跑22個台灣城市
for city in range(22):

    # 將每個地址資料依序做路名比對，判斷此電影院屬於哪一個地區
    # 採由後往前的方式做比對，方便將比對成功的資料從address_col中刪除
    for i in range(len(address_col) - 1, 0, -1):

        # 將地址資料的數字段位改為文字段位，ex:將「1段」改為「一段」
        for sec in range(len(section_num_1)):
            if section_num_1[sec] in address_col[i]:
                address_col[i] = address_col[i].replace(section_num_1[sec],
                                                        section_chi[sec])
                break

        flag = 0
        for j in range(head, tail):

            if city_list_0[city] in address_col[i]:
                if df.iloc[j, 1] in address_col[i]:
                    df.iloc[j, 2] += 1
                    #print(j, df.iloc[j, 1])
                    #print(city_list[city], df.iloc[j, 1], df.iloc[j, 2], address_col[i])
                    address_col.pop(i)
                    break

        for j in range(head, tail):

            road_list = road[df.iloc[j, 0]][df.iloc[j, 1]]

            for k in range(len(road_list)):

                # 將「１段」或「1段」改為「一段」
                for sec in range(len(section_num_1)):
                    if section_num_1[sec] in road_list[k]:
                        road_list[k] = road_list[k].replace(section_num_1[sec],
                                                            section_chi[sec])
                        break
                    if section_num_2[sec] in road_list[k]:
                        road_list[k] = road_list[k].replace(section_num_2[sec],
                                                            section_chi[sec])
                        break

                if road_list[k] in address_col[i]:
                    if city_list_0[city] in address_col[i]:
                        df.iloc[j, 2] += 1
                        #print(j, df.iloc[j, 1])
                        #print("KKK", city_list[city], df.iloc[j, 1], df.iloc[j, 2], address_col[i])
                        address_col.pop(i)
                        flag = 1
                        break

            if flag == 1:
                break

    if city < 21:
        if city == 3:
            head += len(road[city_list[city]])
            tail += len(road[city_list[city + 1]]) + 1
        elif city == 4:
            head += len(road[city_list[city]]) + 1
            tail += len(road[city_list[city + 1]])
        else:
            head += len(road[city_list[city]])
            tail += len(road[city_list[city + 1]])

# df.to_csv(path_or_buf = '/Users/wangyuda/Desktop/project/Cinema/df.csv')

