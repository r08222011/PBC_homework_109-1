#input
#級距個數
num = int(input())
#最少需要購買的食材公斤數
least = int(input())
#設定初始值
amount = 0
num_total = 0
howmany = 0

#迴圈
for i in range(num):
  num_delta = 0
  #級距數量
  num_total = int(input())
  #級距單價
  price = int(input())
  #計算差距
  if howmany > 0:
    if num_total > least:
      num_delta = least - howmany
      amount += price * num_delta
      break
    else:
      num_delta = num_total - howmany      
  else:
    num_delta = num_total
  howmany = num_total
  amount += price * num_delta

#output
print(amount)

