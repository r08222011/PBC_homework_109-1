#輸入資料
full_ticket = int(input())
full_price = int(input())
student_ticket = int(input())
student_price = int(input())
money = int(input())
ticket_limit = int(input())
#計算總張數及總支出
ticket_sum = full_ticket + student_ticket
payment = full_price * full_ticket + student_price * student_ticket
change = money - payment
ticket_remaining = ticket_limit - ticket_sum

#計算尚可購買張數及找零
if ticket_sum > ticket_limit:
  if money >= payment:
    print("$" + str(change))
else:
  if money >= payment:
    print(str(ticket_remaining) + "," + "$" + str(change))
  else:
    print(str(ticket_remaining) + ",")