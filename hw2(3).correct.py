#input
#級距個數
num = int(input())
#最少需要購買的食材公斤數
least = int(input())
#設定初始值
amount = 0
num_total = 0
last_num = 0 #上一個級距數量

#迴圈
for i in range(num):
  num_delta = 0 #設定差距初始值
  #級距數量
  num_total = int(input())
  #級距單價
  price = int(input())
  #計算差距
  if last_num >= 0:
    if num_total >= least:
      num_delta = least - last_num
      amount += price * num_delta
      break
    else:
      num_delta = num_total - last_num      
  else:
    num_delta = num_total
  last_num = num_total
  amount += price * num_delta

#output
print(amount)

