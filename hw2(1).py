#設定input
num = int(input())

#將百位數,十位數,個位數分別設定為a,b,c
a = num // 100
b = (num // 10) - a * 10
c = num - (a*100 + b *10) 

#將不足三位數的數補0
if 9 <  num < 100:
  num *= 10
elif 1 <= num <= 9: 
  num *= 100

#由大到小排序
if a <= b:
  if b <= c:
    big_num = c *100 + b *10 +a
    small_num = a*100 + b *10 +c
  elif c <= a:
    big_num = b *100 + a*10 + c
    small_num = c *100 + a * 10 + b
  elif b >= c >= a:
    big_num = b * 100 + c * 10 + a
    small_num = a * 100 + c * 10 + b
elif a >= b:
  if b >= c:
    big_num = a * 100 + b * 10 + c
    small_num = c * 100 + b * 10 + a
  elif a >= c >= b:
    big_num = a * 100 + c * 10 + b 
    small_num = b *100 + c * 10 + a
  elif c >= a:
    big_num = c * 100 + a * 10 + b
    small_num = b * 100 + a * 10 + c

#大數減小數
num = big_num - small_num
num1 = num

#將百位數,十位數,個位數分別設定為a,b,c
a = num // 100
b = (num // 10) - a * 10
c = num - (a*100 + b *10) 

#將不足三位數的數補0
if 9 < num < 100:
  num *= 10
elif 1 <= num <= 9: 
  num *= 100

#由大到小排序
if a <= b :
  if b <= c:
    big_num = c *100 + b *10 +a
    small_num = a*100 + b *10 +c
  elif c <= a:
    big_num = b *100 + a*10 + c
    small_num = c *100 + a * 10 + b
  elif b >= c >= a:
    big_num = b * 100 + c * 10 + a
    small_num = a * 100 + c * 10 + b
elif a >= b:
  if b >= c:
    big_num = a*100+b*10+c
    small_num = c * 100 + b * 10 + a
  elif a >= c >= b:
    big_num = a*100+c*10+b
    small_num = b *100 + c * 10 + a
  elif c >= a:
    big_num = c *100 + a *10 +b
    small_num = b * 100 + a * 10 + c

#大數減小數
num = big_num - small_num
num2 = num

#將百位數,十位數,個位數分別設定為a,b,c
a = num // 100
b = (num // 10) - a * 10
c = num - (a*100 + b *10) 

#將不足三位數的數補0
if 9 < num < 100:
  num *= 10
elif 1 <= num <= 9: 
  num *= 100

#由大到小排序
if a <= b :
  if b <= c:
    big_num = c *100 + b *10 +a
    small_num = a*100 + b *10 +c
  elif c <= a:
    big_num = b *100 + a*10 + c
    small_num = c *100 + a * 10 + b
  elif b >= c >= a:
    big_num = b * 100 + c * 10 + a
    small_num = a * 100 + c * 10 + b
elif a >= b:
  if b >= c:
    big_num = a*100+b*10+c
    small_num = c * 100 + b * 10 + a
  elif a >= c >= b:
    big_num = a*100+c*10+b
    small_num = b *100 + c * 10 + a
  elif c >= a:
    big_num = c *100 + a *10 +b
    small_num = b * 100 + a * 10 + c

#大數減小數
num = big_num - small_num
num3 = num

#output
print(str(num1) + ',' + str(num2) + "," + str(num3))