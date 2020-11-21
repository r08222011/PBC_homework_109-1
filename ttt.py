#input
n, B = input().split(",")
n = int(n)
B = int(B)
weight = input().split(",")
utility = input().split(",")

#排序
total_weight = 0
total_utility = 0
total_weight_2 = 0
total_utility_2 = 0
num_list = []
num_list_2 = []
weight_last = 0

#換成整數
for i in range(n):
    weight[i] = int(weight[i])
    utility[i] = int(utility[i]) 

"""第一種算法"""
#算CP值
cp = []
cpsort = []
for i in range(n):
    cp.append(utility[i] / weight[i]) #cp值 = 效用 / 重量
    cpsort.append(utility[i] / weight[i]) #把cp值再存進另一個清單，以利之後做計算
    index = i 
#把CP值排序
cpsort.sort()
cpsort.reverse()#由大排到小

for i in range(n-1):
    if float(cp[i]) == float(cp[i+1]):
        #如果cp值相同，先放輕的
        if weight[i] > weight[i+1]:
            num_big = float(cp[i])
            num_small = float(cp[i+1])
            #更換順序
            cpsort[i] = float(num_small)
            cpsort[i+1] = float(num_big)

for i in range(n):
    index = cp.index(cpsort[i]) #找出在排序前是第幾個項目  
    if total_weight + weight[index] <= B: #如果不會超過負重
        total_weight += weight[index]  #更新總重
        total_utility += utility[index] #更新總效用
        num_list.append(int(index + 1)) #更新放進包包的項目
    if total_weight == B: #與最大負重相同時break,不然就繼續看
        break   
#將項目編號排列
num_list.sort()
"""第一種結束"""

"""第二種算法"""
#開另一個效用list，以利之後做計算
usort = []
for i in range(n):
    usort.append(utility[i]) 
usort.sort()
usort.reverse() #小排到大

for i in range(n-1):
    if int(utility[i]) == int(utility[i+1]):
        #如果效用一樣，挑輕的先放
        if weight[i] > weight[i+1]: 
            num_big = int(utility[i])
            num_small = int(utility[i+1])
            #交換順序
            usort[i] = int(num_small)
            usort[i+1] = int(num_big)

#如果有兩個效用一樣
#先創造一個一模一樣的utility list
utility_copy = []
for i in range(n):
    utility_copy.append(utility[i])
indexs = []
#計算包包裡面要放甚麼
for i in range(n):
    index = utility_copy.index(usort[i]) #找出在排序前是第幾個項目  
    if total_weight_2 + weight[index] <= B: #如果不會超過負重
        total_utility_2 += utility[index] #更新總效用
        total_weight_2 += weight[index] #更新總重
        num_list_2.append(index+1) #更新放進包包的項目
    if total_weight_2 + weight[i] ==B:  #與最大負重相同時break,不然就繼續看
        break    
    if usort[i] in utility_copy:
        # 某一個的index
        some_index = utility_copy.index(usort[i])
        indexs.append(some_index)
        # 直接remove 會導致所有index跟著變
        # 所以把找過的設成 -1
        utility_copy[some_index] = -1
#將項目編號排序
num_list_2.sort()
"""第二種算法結束"""

#看哪一種算法效用較大
if total_utility > total_utility_2: #第一種算法較大，print第一種算法的結果
    output = ""
    for i in range(len(num_list)):
        output += str(num_list[i])
        if i != len(num_list) - 1:
            output += ","
elif total_utility_2 >= total_utility: #第二種算法效用較大，或兩者相等，print第二種算法的結果
    output = ""
    for i in range(len(num_list_2)):
        output += str(num_list_2[i]) 
        if i != len(num_list_2) - 1:
            output += ","
 
#output
print(output)