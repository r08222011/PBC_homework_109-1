#設定input
full_ticket_num = int(input())
student_ticket_num = int(input())

full_ticket_price = int(input())
student_ticket_price = int(input())
#設定金額及找錢數目
pay = int(input())
price_sum = full_ticket_num * full_ticket_price + student_ticket_num * student_ticket_price
change = pay - price_sum
print(str(pay) + ',' + str(price_sum) + ',' + str(change))