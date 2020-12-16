
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


final_score = 0



suit = input().split(",")
rank = input().split(",")

# c1 = Card(suit=suit[0], rank=rank[0])
# print(c1.suit)

c = []
for i in range(5):
    c.append(Card(suit=suit[i], rank=rank[i]))
    # print(c[i].suit)

#同花順
    
# def suit_criteria(c_element):
flower = []
# c_element is element in c
for i in range(5):
    if c[i].suit == "S":
        flower.append(4)
    elif c[i].suit == "H":
        flower.append(3)
    elif c[i].suit == "D":
        flower.append(2)
    elif c[i].suit == "C":
        flower.append(1) 
flower.sort(reverse=True)
# print(flower)
    # print(num)

# def rank_criteria(c_element):
number = []
for i in range(5):
    if c[i].rank != "A" and c[i].rank != "J" and c[i].rank != "Q" and c[i].rank != "K":
        number.append(int(c[i].rank))
    elif c[i].rank == "A":
        number.append(1)
    elif c[i].rank == "J":
        number.append(11)
    elif c[i].rank == "Q":
        number.append(12)
    elif c[i].rank == "K":
        number.append(13)
        
number.sort()

#四個花色各出現幾次
list_flower = [0,0,0,0]
for i in range(5):
    if flower[i] == 1:
        list_flower[0] += 1
    elif flower[i] == 2:
        list_flower[1] += 1
    elif flower[i] == 3:
        list_flower[2] += 1
    elif flower[i] == 4:
        list_flower[3] += 1
# print(list_flower)

#點數出現幾次
list_number = [0,0,0,0,0,0,0,0,0,0,0,0,0]
# number = [13,2,12,4,1]
for i in range(5):
    list_number[number[i]-1] += 1
# print(list_number)

#桐花順
result = 1
score = 0
if 5 in list_flower:
    for i in range(4):
        if number[i] == number[i+1] - 1:
            if i == 3:
                result = 0
                score = 100
        else: #不是同花順
            break
#四條
if result == 1:
    for i in range(13):
        if list_number[i] == 4 : #and result == 1
            score += 20
            if list_number[0] == 1:
                score += 1
            result = 0
#葫蘆
# for i in range(13):
if 3 in list_number and 2 in list_number and result == 1:
    result = 0
    score += 10
#順子
index_list = []
good = True
if 2 not in list_number and 3 not in list_number and 4 not in list_number:
    for i in range(13):
        if list_number[i] == 1:
            index_list.append(i)
    # print(index_list)
    for i in range(len(index_list) - 1):
        if index_list[i] +1 ==  index_list[i+1]:
            continue
        else:
            good = False
            break 
else:
    good = False

if number == [1,10,11,12,13]:
    good = True
elif number == [1,2,11,12,13]:
    good = True
elif number == [1,2,3,12,13]:
    good = True
elif number == [1,2,3,4,13]:
    good = True
    
if good and result == 1:
    score += 5
    result = 0
#同花
if result == 1 and 5 in list_flower :
    score += 3
    result = 0
#一對
if result == 1 and (2 in list_number or 3 in list_number ):
    for i in range(13):
        if list_number[i] == 2 or list_number[i] == 3:
            score += 2
        # if list_number[0] >= 2:
    if list_number[0] == 3 or list_number[0] == 1:
        list_number[0] = -100
        score += 1
    result = 0
#一張A
if result == 1 and list_number[0] != 0:
    score += 1

print(score)