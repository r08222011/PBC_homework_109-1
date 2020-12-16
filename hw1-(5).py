#輸入值
concen = int(input())
temp = int(input())
dew_temp = int(input())
value = float(input())

#設定初始赴約意願值
willngness = 0.5
moisture = 100 - 5 * (temp - dew_temp)

#濃度影響
if concen <= 35:
  willingness_concen = willngness + (100 - concen) * 0.005
else:
  willingness_concen = willngness + ( 45 - concen) * 0.02
if willingness_concen  < 0:
  willingness_concen = 0
if willingness_concen > 1:
  willingness_concen = 1
#濕度影響
if moisture < 30:
  willingness_moi = (willngness / 60) * (110 - moisture)
else:
  willingness_moi = (willngness / 45) * (90 - moisture)
if willingness_moi < 0:
  willingness_moi = 0
if willingness_moi > 1:
  willingness_moi = 1
#判斷兩意願值高低
if willingness_moi < willingness_concen:
  willingness_new = willingness_moi
else:
  willingness_new = willingness_concen
print('{:.2f}'.format(willingness_new))
#結論：同意嗎
if willingness_new >= value:
  print("Let's go together.")
else:
  print("I wouldn't go out with you.")
  
  