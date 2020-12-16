#input
n, B, eta = input().split(',')
n = int(n)
B = int(B)
eta = int(eta)
money = input().split(',')
reward = input().split(',')
#initial 
cov = []
matrix = []
max_num = 0
index = 0
index_1 = 0
#
for i in range(n):
    var = input().split(',') 
    for j in range(n):
        #把每個input轉成整數
        var[j] = int(var[j]) 
    #做成一個矩陣
    cov.append(var) 
#轉成整數
for i in range(n):
    reward[i] = int(reward[i])
    money[i] = int(money[i])
    cov[i][i] = int(cov[i][i])

# initial values
total_weight = 0  # total weight
total_value  = 0  # total value
indexs       = [] # 項目的index(從0開始)
#計算
while total_weight < B: #總重低於限重
    #initial values
    current_best_index = -1 
    current_best_value = total_value
    current_best_weight  = -1 # 越高越好
    for some_index in range(n):
        # 檢查該項目是否已被選進,也要檢查加上去是否會超過限重
        if (some_index not in indexs) and (total_weight + money[some_index] <= B):
            # 計算總價值
            value = reward[some_index] - eta*cov[some_index][some_index]
            for index_i in indexs: #已經挑到的項目
                #v_i * x_i
                value += reward[index_i]
                # eta * sigma_ij * x_i * x_j
                value -= 2*eta*cov[index_i][some_index] # *2，因為是對稱矩陣，然後事跟被挑中項目的共變異數
                for index_j in indexs:
                    value -= eta*cov[index_i][index_j] #自己的變異數
            # 檢查是否為最大值
            if value > current_best_value:
                #是的話將該項目存進curren_best組合中
                current_best_index    = some_index
                current_best_value    = value
                current_best_weight = money[some_index]
            #檢查是否有兩個目標函數值相同
            if value == current_best_value and current_best_index != -1: #如果相同且真的有挑到某項目
                if money[some_index] < current_best_weight: #將資金需求較低的項目拿去替換
                    current_best_index    = some_index
                    current_best_value    = value
                    current_best_weight = money[some_index]


    #如果沒有辦法挑種任何投資標的
    if current_best_index == -1:
        break
    # 如果有挑中投資標的
    else: 
        #更新資料
        total_weight += money[current_best_index]
        indexs.append(current_best_index)
        total_value = current_best_value

# output
if len(indexs) == 0: #沒有挑中任何投資標的，print 0
    print(0)
else: #有挑中至少一種投資標的
    indexs.sort() #將項目編號由小到大排序
    output = ""
    for i in range(len(indexs)):
        output += str(indexs[i]+1) # 需加一才是現實世界的項目編號
        if i != len(indexs) - 1: #如果不是最後一項，加逗號
            output += ","
    print(output)
