import pandas as pd

path = "/Users/yianchen/Desktop/eat.csv"
df = pd.read_csv(path, header=None, encoding="utf-8")
money = df[3].values.tolist()



for i in range(1,len(money)):
    try:
        m = int(money[i])
    except:
        if type(money[i])==str and "-" in money[i] and len(money[i])<8:
                money[i] = money[i].split("-")
                money[i][0] = int(money[i][0])
                money[i][1] = int(money[i][1])
    else:
        money[i] = m



# $ 0-100
# $$ 101-200
# $$$ 201-300
# $$$$ 301-500
# $$$$$ 501-

def how_much_money(m):
    if m<=100:
        return "$"
    elif m<=200:
        return "$$"
    elif m<=300:
        return "$$$"
    elif m<=400:
        return "$$$$"
    else:
        return "$$$$$"

money_range = []
for i in range(1,len(money)):
    m = money[i]
    if type(m) == int:
        money_range.append(how_much_money(m))
    elif type(m) == list:
        money_range.append(how_much_money(m[0])+" "+how_much_money(m[1]))
    else:
        money_range.append("")
print(money_range)


df[4][1:] = money_range


df.to_csv("/Users/yianchen/Desktop/output.csv",index=False,encoding="utf-8_sig")