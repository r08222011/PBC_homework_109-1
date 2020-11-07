### 公司 c input
c = input().split(",")

### 關鍵字 d input
d = input().split(",")
### 由於判斷順序是 1.關鍵字長度 2.長度相同就看哪個關鍵字在重疊的部分中先出現
def d_sort_criteria(_string):
    ### 依長度排序，此法同長度的話依然保留前後順序
    return len(_string)
d.sort(reverse=True, key=d_sort_criteria)
### 將 d 依照長度分組
d_group, temp_d, current_len = [], [], len(d[0])
for i in range(len(d)):
    if len(d[i]) == current_len:
        temp_d.append(d[i])
    else:
        d_group.append(temp_d)
        temp_d, current_len = [d[i]], len(d[i])
    if i == len(d)-1:
        d_group.append(temp_d)

### 標題 t input 
t = []
while True:
    _input = input()
    if _input == "INPUT_END":
        break
    ### 把空格都弄掉
    _input = _input.split()
    _output = ""
    for element in _input:
        _output += element
    t.append(_output)

### define 一個函數處理每行的關鍵字
def get_splited(line): ### 輸入為某行標題
    splited = [line] ### 先初始化為一個list
    for d_list in d_group:
        temp_splited = []
        for sentence in splited:
            if sentence in d:
                ### 代表此sentence已是關鍵字
                temp_splited.append(sentence)
            else:
                ### 代表此sentence不是關鍵字
                while sentence != "":
                    best_index = -1
                    for keyword in d_list:
                        if keyword  in sentence:
                            if best_index == -1:
                                best_index = sentence.index(keyword)
                            elif sentence.index(keyword) < best_index:
                                best_index = sentence.index(keyword)
                    if best_index == -1: ### sentence裡沒有keyword
                        temp_splited.append(sentence)
                        sentence = ""
                    else:
                        keyword_len = len(d_list[0]) ### d_list 每個元素都一樣長
                        if sentence[:best_index] != "":
                            temp_splited.append(sentence[:best_index])
                        temp_splited.append(sentence[best_index:best_index+keyword_len])
                        sentence = sentence[best_index+keyword_len:]
        splited = temp_splited
    ### 將最後的結果依照"/"串在一起
    final_splited = ""
    for i in range(len(splited)):
        final_splited += splited[i]
        if i != len(splited)-1:
            final_splited += "/"
    return final_splited

### define 一個等等排序公司的標準
def c_sort_criteria(_list):
    return _list[1]
### 開始處理每行標題
for line in t:
    ### 先檢查line裡有沒有公司名字，若無則NO_MATCH
    c_in_line = []
    for company in c:
        if company in line:
            ### append [company,0], 0為等等紀錄出現次數
            c_in_line.append([company,0])
    if len(c_in_line) == 0: ### NO_MATCH
        print("NO_MATCH")
    else: ### HAS_MATCH
        splited_line = get_splited(line)
        ### 記錄每間公司出現次數
        for i in range(len(c_in_line)):
            c_in_line[i][1] = splited_line.count(c_in_line[i][0])
        ### 將公司依出現次數排序
        c_in_line.sort(reverse=True, key=c_sort_criteria)
        ### 處理output
        output = ""
        for i in range(len(c_in_line)):
            output += c_in_line[i][0]
            if i != len(c_in_line)-1:
                output += ","
            else:
                output += ";"
        output += splited_line
        print(output)