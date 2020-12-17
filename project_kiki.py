import pandas as pd
import random

def load_data():
    path = "/Users/yianchen/Desktop/Programming/KiKi_Python_HW/eattttt.csv"
    df = pd.read_csv(path, header=None, encoding="utf-8")
    # 去除標題
    df = df[1:]
    return df

def money_selection(df, money_range):
    money_list = df[4].tolist()
    money_list = [money_list[i].split(" ") for i in range(len(money_list))]
    money_bool = [False for i in range(len(money_list))]
    for i in range(len(money_list)):
        for money in money_range:
            if money in money_list[i]:
                money_bool[i] = True
                break
    return df[money_bool]

def place_selection(df, place_range):
    place_list = df[1].tolist()
    place_bool = [False for i in range(len(place_list))]
    for i in range(len(place_list)):
        for place in place_range:
            if place == place_list[i]:
                place_bool[i] = True
                break
    return df[place_bool]

def type_selection(df, type_range):
    type_list = df[5].tolist()
    type_bool = [False for i in range(len(type_list))]
    for i in range(len(type_list)):
        for food_type in type_range:
            if food_type == type_list[i]:
                type_bool[i] = True
                break
    return df[type_bool]

# random
def random_pick(df, number):
    df_list = df[0].tolist()
    number = min(number, len(df_list))
    result = random.sample(df_list, number)
    selection_bool = [False for i in range(len(df))]
    for i in range(len(selection_bool)):
        for name in result:
            if name == df_list[i]:
                selection_bool[i] = True
                break
    return df[selection_bool].reset_index()


# print the result
def print_result(number):
    for i in range(min(len(result),number)):
        target = result.loc[i]
        print(f"---------------------------------------------------------")
        print(f"推薦您的第 {i+1} 家餐廳資訊如下：")
        print(f"餐廳：{target[0]}")
        print(f"地址：{target[2]}")
        print(f"價位：{target[3]}")
    print(f"---------------------------------------------------------")

################################################################
############                                       #############
############                主程式開始               #############
############                                       #############
################################################################

# initial
df = load_data()
number = 10
money_range = ["$"]
place_range = ["公館1","公館2","公館+水源"]
type_range = ["日式","西式"]

# select
df_select = df.copy()
df_select = money_selection(df_select, money_range)
df_select = place_selection(df_select, place_range)
df_select = type_selection(df_select, type_range)

# random choose
result = random_pick(df_select,number)

# print the result
print_result(number)