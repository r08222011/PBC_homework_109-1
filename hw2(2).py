#input
least = int(input())
#級距數量
num1 = int(input())
#各級單價
price1 = int(input())
#級距數量
num2 = int(input())
#各級單價
price2 = int(input())
#級距數量
num3 = int(input())
#各級單價
price3 = int(input())

#計算總支出
if least > num3:
  amount = num1 * price1 + (num2 - num1) * price2 + (num3 - num2) * price3
elif num2 < least <= num3:
  amount = num1 * price1 + (num2 - num1) * price2 + (least - num2) * price3
elif num1< least <= num2:
  amount = num1 * price1 + (least - num1) * price2
elif least <= num1:
  amount = least * price1 

#output
print(amount)