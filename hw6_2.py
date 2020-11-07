### 處理所有input
w, k1, k2 = int(input()), input(), input()
sentences = []
while True:
    _input = input()
    if _input == "INPUT_END":
        break
    sentences.append(_input.strip())

### 將所有句子合成成 S
S = ""
for i in range(len(sentences)):
    S += sentences[i]
    if i != len(sentences)-1:
        S += " "

### 找出所有包含 k1, k2 的 index
def indices_of_k(k): ### 這裡的k可以是k1或k2
    start_index = 0
    indices = []
    while k in S[start_index:]: ### 如果關鍵字k在S的sub-string中
        ### 搜尋從start_index到len(S)中第一個出現k的index
        next_index = S.index(k, start_index, len(S))
        indices.append(next_index)
        ### 然後再把start_index往後調，以免重複算
        start_index = next_index + 1
    return indices

k1_indices = indices_of_k(k1) ### 所有k1的index
k2_indices = indices_of_k(k2) ### 所有k2的index

### 自己define 一個 max 函數
def max(x,y):
    return x if (x > y) else y

### 開始找尋符合的句子
NO_MATCH = True ### 如果都沒有符合就會維持True
for k1_i in k1_indices:
    for k2_i in k2_indices:
        ### 如果k2的index比k1的index小，就不用處理，因為k1應在k2前面
        if k1_i >= k2_i:
            continue
        ### 兩個keyword中的間格指的是k1結束到k2開始之前中間的字元數
        elif k2_i - (k1_i + len(k1)) <= w:
            ### 進入此迴圈代表有解
            NO_MATCH = False
            output = ""
            output += S[max(0,k1_i-7):k1_i]              ### 前七個字
            output += "**" + k1 + "**"                   ### 第一個keyword
            output += S[k1_i+len(k1):k2_i]             ### 中間的字
            output += "**" + k2 + "**"                   ### 第二個keyword
            output += S[k2_i+len(k2):k2_i+len(k2)+7] ### 最後七個字
            print(output)
        elif k2_i - (k1_i + len(k1)) > w:
            break
if NO_MATCH:
    print("NO_MATCH")