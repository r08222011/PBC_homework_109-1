# 寫一個 Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        # 處理 A,J,Q,K
        if rank == "A":
            self.rank = 1
        elif rank == "J":
            self.rank = 11
        elif rank == "Q":
            self.rank = 12
        elif rank == "K":
            self.rank = 13
        else:
            self.rank = int(rank)
# 寫一個 Deck class
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        # 這邊要求>0是因為之後牌不夠，我會新增rank是負數的牌填充
        if self.cards != [] and card.rank > 0:
            for i in range(len(self.cards)):
                # mod 13 是因為要比較K的特殊情況
                if self.cards[i].suit == card.suit and (self.cards[i].rank + 1)%13 == card.rank%13:
                    del self.cards[i]        
                    break
                elif i == len(self.cards)-1:
                    self.cards.append(card)
        else:
            self.cards.append(card)

def score(deck):
    c = deck.cards

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
        else:
            flower.append(0)
    flower.sort(reverse=True)
    # print(flower)
        # print(num)

    # def rank_criteria(c_element):
    number = []
    for i in range(5):
        number.append(c[i].rank)
            
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
        if number[i] > 0:
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
    if result == 1 and sum(list_number) == 5:
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
    if 2 not in list_number and 3 not in list_number and 4 not in list_number and sum(list_number) == 5:
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
    return score

# input n
n = int(input())
output = ""
for i in range(n):
    # initialize a Deck class
    deck = Deck()
    # split into list
    input_cards = input().split(",")
    # 將每個element轉換成Card
    input_cards = [Card(input_cards[i][0],input_cards[i][1:]) for i in range(9)]

    # 開始依序加入手牌
    for j in range(9):
        deck.add_card(input_cards[j])
        if len(deck.cards) == 5:
            break

    # 若牌數不足五張，則新增補充牌，花色為Ancilla，數字為負數，以免等等算分搞混
    for j in range(5):
        if len(deck.cards) < 5:
            deck.add_card(Card("Ancilla",-2*j-1))
        else:
            break
    
    # 處理ouput格式
    output += str(score(deck))
    if i != n-1:
        output += ","
print(output)