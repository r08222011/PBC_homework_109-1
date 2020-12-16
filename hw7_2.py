#讀檔
file1 = "C:\\Users\\A315\\Downloads\\u.item"
item = open(file1, 'r', encoding = 'utf-8')
file2 = "C:\\Users\\A315\\Downloads\\u.genre"
genre = open(file2, 'r', encoding = 'utf-8')

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for combination in zip(a, genre):
    print(combination)