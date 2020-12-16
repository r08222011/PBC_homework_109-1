#initial value
records = []
search_list = []

#input
for i in range(100):
    temp = input()
    if temp != "RECORDSTOP": 
        #如果輸入不是"RECORDSTOP"就以逗號隔開加進清單
        temp_list = temp.split(",")
        for j in range(1,5): 
            #將1~4項資料轉成整數
            temp_list[j] = int(temp_list[j])
        records.append(temp_list) #把資料加進records
    elif temp == "RECORDSTOP": 
        #如果輸入是"RECORDSTOP"就break
        break

#要查的資料
for i in range(100):
    search = input()
    if search != "FUNCTIONSTOP": 
        #如果輸入不是"FUNCTIONSTOP"就以空格隔開加進清單
        search = search.split()
        #再加入search_list
        search_list.append(search)
    elif search == "FUNCTIONSTOP":
        #如果輸入是"FUNCTIONSTOP"就break
        break

#define無條件捨去的函數
def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0

#處理年分
for i in range(len(search_list)):
    if "," in search_list[i][1]: 
        #如果輸入的年分那項中間有逗號(代表查的是兩年以上的資料)，將其以逗號隔開
        search_list[i][1] = search_list[i][1].split(",")
        #再把年分的每一項轉成整數
        search_list[i][1] = [int(k) for k in search_list[i][1]]
    elif "," not in search_list[i][1]:
        #如果輸入的年分那項中間沒有逗號，那就直接轉成整數就好
        search_list[i][1] = [int(search_list[i][1])]        

#define球員打擊率
def player_avg(seasons, player_number): #參數
    #初始值
    anda = 0
    play = 0
    for i in range(len(records)):
        if player_number == int(records[i][1]): #找到要找的球員號碼
            for k in range(len(seasons)): #針對年分
                if seasons[k] == records[i][2]: #找到要找的年份
                    anda += records[i][4] #安打累積數
                    play += records[i][3] #打數累積數
    #打擊率=安打/打數，如果打數等於0的話直接設為0
    strike = anda / play if play != 0 else 0 
    #無條件捨去
    strike = chop(strike)
    #print
    print(strike)

#player_avg(seasons=search_list[0][1], player_number=search_list[0][2])

#define球隊打擊率
def team_avg(seasons, team_name):
    #初始值
    anda = 0
    play = 0
    for i in range(len(records)):
        if team_name == (records[i][0]): #找到要找的球隊
            for k in range(len(seasons)): #針對年分
                if seasons[k] == (records[i][2]): #找到要找的年份
                    anda += records[i][4] #安打累積數
                    play += records[i][3] #打數累計數
    #團隊打擊率=總安打數/總打數，如果分母等於0就將打擊率直接設為0
    team_strike = anda / play if play != 0 else 0
    #無條件捨去
    team_strike = chop(team_strike)
    #print
    print(team_strike)
#team_avg(seasons=search_list[0][1], team_name=search_list[0][2])

#找出表現最佳球員
def best_player(seasons):
    #初始值
    best = []
    for i in range(len(seasons)):
        #初始值
        max_compare = -1
        min_play = 10000000
        min_number = 10000000
        for j in range(len(records)):
            if records[j][2] == seasons[i]: #找到要找的年份
                #計算打擊率，如果分母等於0就將打擊率設為0
                strike = records[j][4] / records[j][3] if records[j][3] != 0 else 0
                #比大小
                if strike == max_compare: #打擊率一樣的話
                    #選入打數較少的球員；如果打數一樣，選號碼小的
                    if (records[j][3] < min_play) or (records[j][3] == min_play and records[j][1] < min_number):
                        max_compare = strike #更新較高的打擊率
                        min_play = records[j][3] #更新較少的打數
                        min_number = records[j][1] #更新較小的球員號碼
                elif strike > max_compare: #如果打擊率大於目前最大的
                    max_compare = strike #更新打擊率
                    min_play = records[j][3] #更新打數
                    min_number = records[j][1] #更新球員號碼
        #將最佳球員的號碼加進best清單
        best.append(min_number)
    #output
    output = ""
    for m in range(len(best)):
        output += str(best[m])
        #如果不是最後一項，加逗號
        if m != len(best) - 1: 
            output += ","
    #print
    print(output)
#best_player(seasons=search_list[i][1])

#最佳表現球隊
def best_team(seasons):
    #初始值
    best = []
    for i in range(len(seasons)):
        #初始值
        #將每隊(最多A~Z)安打及打數初始值都設為0
        anda_list = [0 for k in range(26)]
        play_list = [0 for k in range(26)]
        #隊伍名稱清單
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_list = list(alphabet)
        for j in range(len(records)):
            if records[j][2] == seasons[i]:  #找到要找的年份
                index = alphabet_list.index(records[j][0]) #找到要找的球隊
                anda_list[index] += records[j][4] #累計安打數
                play_list[index] += records[j][3] #累計打數
        #打擊率清單
        strike_list = []
        for j in range(26):
            if play_list[j] != 0: #如果打數不為0         
                #將計算打擊率再加進打擊率清單  
                strike_list.append(anda_list[j]/play_list[j])
            else: #打數為0
                #不做比較，故將其打擊率設為-1
                strike_list.append(-1)
        #初始值        
        min_play = 10000
        max_strike = -1
        index = ""
        for j in range(len(strike_list)):
            if strike_list[j] > max_strike: #如果打擊率比目前最大的大
                max_strike = strike_list[j] #更新打擊率
                min_play = play_list[j] #更新打數
                index = alphabet_list[j] #更新球隊
            elif strike_list[j] == max_strike: #如果一樣的話
                if play_list[j] < min_play: #選入打數少的
                    min_play = play_list[j] #更新打數
                    index = alphabet_list[j] #更新球隊
            #而如果打數還是一樣，不需做調整，因為原本的清單就已經是從球隊字母排序的先排了
        #將最佳球隊嘉進best清單
        best.append(index) 
    #output
    output = ""
    for m in range(len(best)):
        output += str(best[m])
        if m != len(best) - 1: #如果不是最後一項，加逗號
            output += ","
    #print
    print(output)


#best_team(seasons=search_list[i][1])

#最終output
for i in range(len(search_list)):
    if search_list[i][0] == "1": #如果要搜的是1
        #算球員打擊率
        player_avg(seasons=search_list[i][1], player_number=int(search_list[i][2]))
    elif search_list[i][0] == "2": #如果要搜的是2
        #算球隊打擊率
        team_avg(seasons=search_list[i][1], team_name=(search_list[i][2]))
    elif search_list[i][0] == "3": #如果要搜的是3
        #算最佳表現球員
        best_player(seasons=search_list[i][1])
    elif search_list[i][0] == "4": #如果要搜的是4
        #算最佳表現球隊
        best_team(seasons=search_list[i][1])
