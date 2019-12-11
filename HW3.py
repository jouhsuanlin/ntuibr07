# Week7 HW3


# 1.建構 sales_sum() 函數
def sales_sum(product_cnt, day_cnt, quantities, prices):
    sum_all = 0
    # 依商品種類逐項計算
    for i in range(product_cnt):
        sum_product = 0
        # 依時間逐期計算
        for j in range(day_cnt):
            # 計算各期銷售額
            sales = prices[i] * quantities[i][j]
            # 累加某商品各期銷售額
            sum_product += sales
        # 累加各商品銷售額
        sum_all += sum_product
    return sum_all


# 2.建構 daily_sales() 函數
def daily_sales(product_cnt, day_cnt, quantities, prices):
    # 建立一個空清單，用來記錄 daily_sales
    list0 = list()
    # 依時間逐期計算
    for i in range(day_cnt):
        sum_daily_salse = 0
        # 依商品種類逐項計算
        for j in range(product_cnt):
            # 計算某商品該期銷售額
            sales = prices[j] * quantities[j][i]
            # 累加某期所有商品銷售額
            sum_daily_salse += sales
        # 記錄 daily_sales
        list0.append(sum_daily_salse)
    return list0


# 3.建構 daily_avg() 函數
def daily_avg(product_cnt, day_cnt, quantities, prices):
    # 直接套用 sales_sum 函數算平均
    average = sales_sum(product_cnt, day_cnt, quantities, prices) / day_cnt
    return average


# 4.建構 goods_sales() 函數
def goods_sales(product_cnt, day_cnt, quantities, prices):
    # 建立一個空清單，用來記錄 goods_sales
    list0 = list()
    # 依商品種類逐項計算
    for i in range(product_cnt):
        sum_product = 0
        # 依時間逐期計算
        for j in range(day_cnt):
            sales = prices[i] * quantities[i][j]
            sum_product += sales
        # 記錄 goods_sales
        list0.append(sum_product)
    return list0


# 5.建構 goods_avg() 函數
def goods_avg(product_cnt, day_cnt, quantities, prices):
    # 建立一個空清單，用來記錄 goods_avg
    list0 = list()
    # 依商品種類逐項計算
    for i in range(product_cnt):
        sum_product = 0
        # 依時間逐期計算
        for j in range(day_cnt):
            sales = prices[i] * quantities[i][j]
            sum_product += sales
        # 計算平均
        average = sum_product / day_cnt
        # 記錄 goods_avg
        list0.append(average)
    return list0


# 6.建構 best_day() 函數
def best_day(product_cnt, day_cnt, quantities, prices):
    # 套用 daily_sales 函數，得到每天的銷售額清單
    daily_sales_list = daily_sales(product_cnt, day_cnt, quantities, prices)
    # 令最佳星期幾與最佳銷售額為 0，用來記錄
    best_weekdays = 0
    best_salse = 0
    # 依星期幾逐日計算（從週一開始）
    for i in range(0, 7):
        # 令某星期幾的次數與該星期幾的銷售額為 0，用來記錄
        weekdays_count = 0
        weekdays_sales = 0
        # 固定星期幾，逐週計算
        for j in range(i, len(daily_sales_list), 7):
            # 計算有幾個星期幾
            weekdays_count += 1
            # 累加該星期幾的銷售額
            weekdays_sales += daily_sales_list[j]
        # 若某星期幾的數量不為 0
        if weekdays_count != 0:
            # 直接計算平均
            weekdays_average_sales = weekdays_sales / weekdays_count
        # 若某星期幾的數量為 0
        else:
            # 直接給定該星期幾的銷售額為 0
            weekdays_average_sales = 0
        # 記錄最佳銷售額與最佳星期幾
        if best_salse < weekdays_average_sales:
            best_salse = weekdays_average_sales
            best_weekdays = i
    return (best_weekdays + 1)


# 設定第一行商品個數與時間期數的輸入
input_list = input().split(",")

for i in range(len(input_list)):
    input_list[i] = int(input_list[i])

n = input_list[0]
t = input_list[1]


# 設定第二行價格的輸入
price_list = input().split(",")

for i in range(len(price_list)):
    price_list[i] = int(price_list[i])


# 設定各商品每日銷售量的輸入
quantity_list = list()
for i in range(n):
    quantity_list.append(input().split(","))

for i in range(n):
    for j in range(t):
        quantity_list[i][j] = int(quantity_list[i][j])


# 設定欲分析項目編號的輸入
number_list = input().split(",")

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])


# 根據指定項目，輸出分析結果
for i in range(len(number_list)):
    # 1.sales_sum
    if number_list[i] == 1:
        print(sales_sum(n, t, quantity_list, price_list))

    # 2.daily_sales
    elif number_list[i] == 2:
        list0 = daily_sales(n, t, quantity_list, price_list)
        for i in range(len(list0)):
            if i != (len(list0) - 1):
                print(list0[i], end=",")
            else:
                print(list0[i])

    # 3.daily_avg
    elif number_list[i] == 3:
        print(int(daily_avg(n, t, quantity_list, price_list)))

    # 4.goods_sales
    elif number_list[i] == 4:
        list0 = goods_sales(n, t, quantity_list, price_list)
        for i in range(len(list0)):
            if i != (len(list0) - 1):
                print(list0[i], end=",")
            else:
                print(list0[i])

    # 5.goods_avg
    elif number_list[i] == 5:
        list0 = goods_avg(n, t, quantity_list, price_list)
        for i in range(len(list0)):
            if i != (len(list0) - 1):
                print(int(list0[i]), end=",")
            else:
                print(int(list0[i]))

    # 6.best_day
    elif number_list[i] == 6:
        print(best_day(n, t, quantity_list, price_list))
