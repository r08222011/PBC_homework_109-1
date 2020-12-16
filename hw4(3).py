#input
n, B = input().split(",")
n = int(n)
B = int(B)
weight = input().split(",")
utility = input().split(",")

#initial vlaues
total_weight = 0
total_utility = 0
total_weight_2 = 0
total_utility_2 = 0
num_list = []
num_list_2 = []
weight_last = 0
#轉成整數
for i in range(n):
    weight[i] = int(weight[i])
    utility[i] = int(utility[i]) 

"""第一種算法"""
#算CP值
cp = []
cpsort = []
for i in range(n):
    cp.append(utility[i] / weight[i]) #效用除以重量=cp值
    cpsort.append(utility[i] / weight[i]) #把它存到另一個list
    index = i 
#把CP值排序
cpsort.sort() 
cpsort.reverse() #由大排到小
#如果有兩個項目cp值相同，挑重量輕的先放
for i in range(n-1):
    if float(cp[i]) == float(cp[i+1]):
        #如果前面的比較輕
        if weight[i] > weight[i+1]: 
            num_big = float(cp[i])
            num_small = float(cp[i+1])
            #交換位置放
            cpsort[i] = float(num_small) 
            cpsort[i+1] = float(num_big)

for i in range(n):
    index = cp.index(cpsort[i]) #找出在排序前是第幾個項目  
    if total_weight + weight[index] <= B: #如果沒超出限重
        total_weight += weight[index] #總重量更新
        total_utility += utility[index] #總效用更新
        num_list.append(int(index + 1)) #將真實編號存進num_list
    if total_weight == B: #與最大負重相同時break,不然就繼續看
        break 

#將項目編號排列
num_list.sort()
"""第一種結束"""
"""第二種算法"""
#增加一個效用清單，以利之後做計算
usort = []
for i in range(n):
    usort.append(utility[i])
usort.sort()
usort.reverse() #小排到大
#如果效用一樣，先挑輕的放
for i in range(n-1):
    if int(utility[i]) == int(utility[i+1]):
        if weight[i] > weight[i+1]:
            num_big = int(utility[i])
            num_small = int(utility[i+1])
            #輕的先放
            usort[i] = int(num_small)
            usort[i+1] = int(num_big)

#如果有兩個效用一樣
#先創造一個一模一樣的utility list
utility_copy = []
for i in range(n):
    utility_copy.append(utility[i])
indexs = []
for i in range(n):
    index = utility_copy.index(usort[i]) #找出在排序前是第幾個項目  
    if total_weight_2 + weight[index] <= B: #如果未超出負重
        total_utility_2 += utility[index] #總效用更新
        total_weight_2 += weight[index] #總重量更新
        num_list_2.append(index+1) 
    if total_weight_2 + weight[i] ==B:#與最大負重相同時break,不然就繼續看
        break
#將項目編號排序
num_list_2.sort()
#看哪一種算法效用較大，當作output
if total_utility > total_utility_2: #第一種算法效用較大
    output = ""
    for i in range(len(num_list)):
        output += str(num_list[i])
        #最後一個數字後不用逗號
        if i != len(num_list) - 1: 
            output += ","
elif total_utility_2 >= total_utility: #第二種算法效用較大，或是相等，都print第二種算法的結果
    output = ""
    for i in range(len(num_list_2)):
        output += str(num_list_2[i]) 
        #最後一個數字後不用逗號
        if i != len(num_list_2) - 1:
            output += ","
 
#output
print(output)