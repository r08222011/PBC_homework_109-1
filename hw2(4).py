#input
sleeping_days = int(input())
#設定初始值
lemon_face = 0
honey_face = 0
egg_face = 0
sleep_total = 0
  
#
for i in range(sleeping_days):
  sleeping_hours = float(input())#睡眠時數input
  sleep_total += sleeping_hours
  if sleeping_hours > 7:
    lemon_face += 1
#平均睡眠時間是否超過6小時
if sleep_total / sleeping_days <= 6:
  honey_face = sleeping_days - lemon_face
elif sleep_total / sleeping_days > 6:
  egg_face = sleeping_days - lemon_face
#計算需消耗材料
lemon = lemon_face * 1.5 
honey = honey_face * 18 + egg_face * 6
oil = lemon_face * 4 + honey_face * 9
egg = egg_face * 2
#要買多少
#檸檬
if (lemon * 10 - 5) % 10 == 0: #如果是小數，無條件進位
  buy_lemon = int(lemon + 0.5)
else:
  buy_lemon = lemon
#蜂蜜
buy_honey = honey 
#雞蛋盒數
if egg % 3 != 0:
  buy_egg = (egg // 3) + 1 #如果有小數，無條件進位
else:
  buy_egg = int(egg / 3) #不是小數，不用動
#油
buy_oil = oil 

#分別支出
#檸檬
if buy_lemon >= 5:
  pay_lemon = buy_lemon * 7 * 0.9
else:
  pay_lemon = buy_lemon * 7
#蜂蜜
pay_honey = buy_honey *1.2
#雞蛋
pay_egg = buy_egg * 25
#油
pay_oil = buy_oil * 0.6

#總支出
pay = (pay_lemon + pay_egg + pay_honey + pay_oil)
if pay *10 % 10 != 0:
  pay = int((pay *10) // 10)
else:
  pay = int(pay) 

#output
print(pay)
  