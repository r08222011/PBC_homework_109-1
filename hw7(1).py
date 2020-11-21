#input
read = input()
target = str(input())
if read == "local":
    read = "/Users/yianchen/Desktop/kiki_hw/Gossiping-QA-Dataset.txt"

#讀檔
def get_file_info(file_name):
    _file = open(file_name, "r", encoding = 'utf-8') # 以讀取模式打開
    _file_list = _file.readlines() # 讀取所有行數
    _file_list = [line.strip(" \n") for line in _file_list] # 將換行符號去除
    _file.close() # 關掉檔案
    return _file_list
data = get_file_info(read)

#把句子放進清單
words_list = []

for sentence in data:
    words_list.append(sentence.split('\t'))
    
final_list = []
for i in range(len(words_list)):
    final_list.append(words_list[i][0].strip(" "))
    final_list.append(words_list[i][1].strip(" "))

target_dict = {}
target_dict_before = {}

for i in range(len(final_list)):
    current_index = 0
    while current_index <= len(final_list[i])-1 and target in final_list[i][current_index:]:
        index = final_list[i][current_index:].index(target)+current_index
        # after
        if index+len(target)-1 < len(final_list[i])-1: # 如果關鍵字的最後一個字是整串的最後一個字
            word = final_list[i][index+len(target)]
            if word in target_dict:
                target_dict[word] += 1
            else:
                target_dict[word] = 1
        # before
        if index != 0 or current_index != 0:
            word = final_list[i][index-1]
            if word in target_dict_before:
                target_dict_before[word] += 1
            else:
                target_dict_before[word] = 1
        current_index += index + 1
# print(target_list)

#比哪個字是熱門後一個字
b = list(target_dict.items())


#比哪個是熱門前一個字
before = list(target_dict_before.items())


#熱門前一個字
print("熱門前一個字:")
num = -1
m = 0
compare_list = []
def compare(_tuple):
    return(_tuple[1], _tuple[0])
before.sort(reverse=True, key=compare)
#熱門下一個字
b.sort(reverse=True, key=compare)
#
if len(before) >= 10:
    for i in range(10):
        # if before[i][1] != num and before[i][1] != before[i+1][1]:
            output = ''
            output += (before[i][0]) + "---"
            output += str(target)
            num = before[i][1]
            print(output)
else:
    #按文字內碼排序
    for i in range(len(before)):
        output = ''
        output += (before[i][0]) + "---"
        output += str(target) 
        num = before[i][1]
        print(output)

#熱門下一個字
print("熱門下一個字:")

if len(b) >= 10:
    for i in range(10):
        output = ''
        output += str(target) + "---"
        output += (b[i][0]) 
        print(output)
else:
    for i in range(len(b)):
        output = ''
        output += str(target) + "---"
        output += (b[i][0]) 
        print(output)



