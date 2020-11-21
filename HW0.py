
# 輸入日期
day1 = int(input())
day2 = int(input())
day3 = int(input())
day4 = int(input())
set_day = int(input())

#計算日期間隔
delta_1 = day2 - day1
delta_2 = day3 - day2
delta_3 = day4 - day3

#計算乘積
delta_product = delta_1 * delta_2 * delta_3

#計算停課次數
stop_day = 0
if delta_1 <= 14:
  stop_day += 1
if delta_2 <= 14:
  stop_day += 1 
if delta_3 <= 14:
  stop_day += 1
  
#印出答案
print( str(delta_1) + "," + str(delta_3) + "," + str(delta_product) + ";" + str(stop_day))

#2.
stop_day = 0
if delta_1 <= set_day:
  stop_day += 1
if delta_2 <= set_day:
  stop_day += 1 
if delta_3 <= set_day:
  stop_day += 1
