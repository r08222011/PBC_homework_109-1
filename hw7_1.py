#input
target = str(input())

#讀檔
path = "/Users/yianchen/Desktop/kiki_hw/Gossiping-QA-Dataset.txt"
# data = open(words, 'r', encoding = 'utf-8')
def get_file_info(file_name):
    _file = open(file_name, "r", encoding = 'utf-8') # 以讀取模式打開
    _file_list = _file.readlines() # 讀取所有行數
    _file_list = [line.strip("\n") for line in _file_list] # 將換行符號去除
    _file.close() # 關掉檔案
    return _file_list
data = get_file_info(path)

#把句子放進清單
words_list = []
a = 0


for sentence in data:
    a += 1
    # words_list = [words_list.strip("\n") in words_list]
    words_list.append(sentence.split('\t'))
    
final_list = []
for i in range(len(words_list)):
    final_list.append(words_list[i][0])
    final_list.append(words_list[i][1])

target_list = []
for i in range(len(final_list)):
    if target in final_list[i]:
        index = final_list[i].index(target)
        if index + len(target) <= (len(final_list[i])-1):
            target_list.append(final_list[i][index+len(target)])
            # print(target_list)
        else:
            target_list.append(final_list[i][index:len(final_list[i])])
        
        
# print(target_list)

#define
def find_words(seq):
    d = dict()
    for element in seq:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d

#比哪個字是熱門後一個字
result = find_words(target_list)
print(result)
b = sorted(result.items(), key=lambda x:x[1])
print(b)
print(type(b))

max=-1
for i in range(len(b)):
    pass
# print(sorted(target_list))

# max_ = -1
# for n in range(len(val)):
#     if val[n] > max_:
#         max_ = val[n]
# print(max_) 

