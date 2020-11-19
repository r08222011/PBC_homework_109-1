# --------------------以下處理四行input-----------------------
# *** 1. 前三行input，將檔案路徑儲存
file_path_title = input()
file_path_dict = input()
file_path_company = input()
# *** 2. 第四行會分別輸入有興趣的產業類別、購買的總張數、每輪的購買張數，分別以半形逗號","分隔
target = input().split(",")
# *** 3. 產業類別為string # 購買的總張數要轉成int # 每輪的購買張數會以":"隔開，以split(":")轉成list。
target_category = target[0] # target_category為有興趣的產業類別
stock_total     = int(target[1]) # stock_total為購買的總張數
stock_ratio     = [int(ratio) for ratio in target[2].split(":")] # stock_ratio為每輪的購買張數

# --------------------以下處理讀取檔案-----------------------
# *** 1. 寫一個讀取檔案的函數，並回傳成list
def get_file_info(file_name):
    _file = open(file_name, "r") # 以讀取模式打開
    _file_list = _file.readlines() # 讀取所有行數
    _file_list = [line.strip("\n") for line in _file_list] # 將換行符號去除
    _file.close() # 關掉檔案
    return _file_list
# *** 2. 取得檔案資料
# ---local---
path = "/Users/yianchen/Desktop/kiki_hw/" # 檔案路徑
news_dict = get_file_info(path+"news_dict.txt")
news_title = get_file_info(path+"news_title.txt")
company_category = get_file_info(path+"company_category.txt")
# ---server---
# news_dict = get_file_info(file_path_dict)
# news_title = get_file_info(file_path_title)
# company_category = get_file_info(file_path_company)

# --------------------以下處理關鍵字辭典：news_dict-----------------------
# *** 1. 將news_dict轉成兩層list儲存，news_dict 原本是[ "關鍵字k1 權重w1", "關鍵字k2 權重w2", ... ]的形式
news_dict = [k_w.split() for k_w in news_dict] # 轉成兩層list [ [關鍵字k1,權重w1], [關鍵字k2,權重w2], ... ]形式
# *** 2. 建立一個只儲存關鍵字的list
d = [k_w[0] for k_w in news_dict] # d為只有關鍵字的list
d.sort(reverse=True, key=len) # 依照長度由大到小排列
# *** 3. 將d依照長度分組。建立d_group為最終分組的list，temp_group為暫存list，current_len為當前長度
d_group, temp_group, current_len = [], [], len(d[0])
for i in range(len(d)):
    if len(d[i]) == current_len: # 比較當前d[i]，符合當前長度便加入temp_group暫存
        temp_group.append(d[i])
    else: # 比較當前d[i]，不符合當前長度便temp_group先加入d_group，再將暫存temp_group和當前長度重置為d[i]相關
        d_group.append(temp_group)
        temp_group = [d[i]]
        current_len = len(d[i])
    if i == len(d)-1: # 最後一輪迴圈要把暫存加入d_group中
        d_group.append(temp_group)
# *** 4. 建立關鍵字的字典，為 { 關鍵字k1:權重w1, 關鍵字2:權重w2, ... }
d_dict = {} # 初始化一個dictionary
for i in range(len(news_dict)): # 對於每個值在 news_dict = [ [關鍵字k1,權重w1], [關鍵字k2,權重w2], ... ] 裡
    d_dict[news_dict[i][0]] = int(news_dict[i][1]) # d_dict[關鍵字k] = 權重w

# --------------------以下處理company-----------------------
# *** 1. 將company_category轉成兩層list儲存，company_category 原本是[ "公司cp1 類別cg1", "公司cp2 類別cg2", ... ]的形式
company_category = [c.split() for c in company_category] # 轉成 [ ["公司cp1,類別cg1"] ,["公司cp2,類別cg2"] , ... ]的形式
# *** 2. 建立一個符合這次有興趣的產業類別的公司list
c = [company[0] for company in company_category if company[1] == target_category]
# *** 3. 由於stock_ratio可能給超過c的長度，我們只需要前len(c)個ratio即可
stock_ratio = stock_ratio[:len(c)]

# --------------------以下處理news_title-----------------------
# *** 1. 將每一行標題的空白全部移除
def remove_space(line):
    line = line.split()
    output = ""
    for word in line:
        output += word
    return output
news_title = list(map(remove_space, news_title))
# *** 2. define 一個函數處理每行的關鍵字分割, arg 為某行標題
def news_title_line_split(line):
    splited = [line] # 先初始化為一個list，此list會一直被迭代更新
    for d_list in d_group: # 從最長的關鍵字群組開始比較
        temp_splited = [] # 暫存器
        for sentence in splited: # 對於每個sentence在splited裡，判斷是否為關鍵字
            if sentence in d: # 代表此sentence已是關鍵字
                temp_splited.append(sentence) # 直接加入暫存器
            else: # 代表此sentence不是關鍵字
                while sentence != "":
                    best_index = -1 # 最前面的關鍵字的index
                    for keyword in d_list:
                        if keyword  in sentence:
                            if best_index == -1: # 表示此keyword是這行第一個找到的關鍵字
                                best_index = sentence.index(keyword)
                            elif sentence.index(keyword) < best_index: # 若此關鍵字的index比之前最好的還前面
                                best_index = sentence.index(keyword)
                    if best_index != -1: # 若不等於-1，表示best_index為最前面的關鍵字
                        keyword_len = len(d_list[0]) # d_list 每個關鍵字都一樣長，隨便取一個當這輪關鍵字長度
                        if sentence[:best_index] != "": # 表示開頭不是關鍵字
                            temp_splited.append(sentence[:best_index]) # 把 "開頭" 到 "關鍵字前的字" 加入暫存器
                        temp_splited.append(sentence[best_index:best_index+keyword_len]) # 把關鍵字加到暫存器
                        sentence = sentence[best_index+keyword_len:] # 將sentence更新成剩下的字，繼續while回圈
                    else: # 若依然是-1，表示sentence裡已經沒有其他keyword
                        temp_splited.append(sentence) # 將剩下句子加回暫存器
                        sentence = "" # 令成""以跳出回圈
        splited = temp_splited # 將 splited 迭代更新
    return splited # 回傳成分割好的list形式，即 [ "分割片段1", "分割片段2", "分割片段3", ... ]

# --------------------以下處理output-----------------------
# *** 1. 建立一個雙層list，儲存公司名稱以及其公司分數
company_rank = [list([company, 0]) for company in c]
# *** 2. 檢查每行標題，算算有哪些公司出現並更新他們的公司分數
for i in range(len(news_title)):
    current_split_title = news_title_line_split(news_title[i]) # 分割好的標題，形式為 [ "分割片段1", "分割片段2", "分割片段3", ... ]
    current_score = 0 # 建立一個變數儲存這個標題的分數
    for word in current_split_title: # 對於每個分割片段(word)
        if word in d: # 如果此分割片段在d裡，即此分割片段為關鍵字
            current_score += d_dict[word] # 在關鍵字字店裡找尋對應的分數並加上current_score
    for j in range(len(company_rank)): # 對於每個公司
        if company_rank[j][0] in news_title[i]: # 如果這家公司出現在原本的標題中(注意：要用為分割的標題檢查，以免公司名稱被分割掉)
            company_rank[j][1] += current_score # 更新此公司的分數
# *** 3. 將company_rank依照分數排序，若相同則以公司名稱的字傳入 sorted(reverse=True) 後的輸出順序排序
def rank_criteria(_list):
    return (_list[1], _list[0]) # 會先比較分數，再比較公司名稱
company_rank.sort(reverse=True, key=rank_criteria)
buy_list = [list([company[0],0]) for company in company_rank] # 建立購買清單，為雙層list
while stock_total > 0 and c != []: # 如果 c == []，表示沒有有興趣的公司
    for i in range(len(stock_ratio)):
        if stock_total >= stock_ratio[i]: # stock_total還夠買
            buy_list[i][1] += stock_ratio[i]
            stock_total -= stock_ratio[i]
        else: # stock_total不夠買了
            buy_list[i][1] += stock_total
            stock_total = 0
# *** 4. 印出output
if c == []: # 如果 c == []，表示沒有有興趣的公司
    print("NO_MATCH")
else:
    for i in range(len(buy_list)):
        if buy_list[i][1] > 0:
            print(buy_list[i][0]+"購買"+str(buy_list[i][1])+"張")