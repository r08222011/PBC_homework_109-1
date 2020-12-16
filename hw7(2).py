#input
item_read = input()
genre_read = input()
movie_id = input()


#讀檔
# path_item = "C:\\Users\\A315\\Downloads\\u.item"
# path_genre = "C:\\Users\\A315\\Downloads\\u.genre"
def get_file_info(file_name):
    _file = open(file_name, "r", encoding = 'ISO-8859-1') # 以讀取模式打開
    _file_list = _file.readlines() # 讀取所有行數
    _file_list = [line.strip("\n") for line in _file_list] # 將換行符號去除
    _file.close() # 關掉檔案
    return _file_list
item = get_file_info(item_read)
genre = get_file_info(genre_read)
# item = get_file_info(path_item)
# genre = get_file_info(path_genre)

#將|去除，並分開
genre_list = []
for j in range(19):
    genre_list.append(genre[j].split('|'))    
item_list = []
for j in range(len(item)):
    item_list.append(item[j].split('|'))
#把電影代表屬於某個類別匯入movie_genre清單
movie_genre = []
for j in range(len(item)):
    if movie_id == item_list[j][0]: #找某部片的資料
        movie = item_list[j][1] 
        for index in range(5, 24): #從5開始才是類別
            #如果是1，代表屬於該電影類別，存進清單
            if item_list[j][index] == "1": 
                #把該類別-5(因為要變得跟item的index一樣)
                movie_genre.append(index-5)

#處理輸出的資料
output = []
for index in movie_genre:
    for j in range(len(genre_list)):
        #將電影所屬的類別加進output
        if index == int(genre_list[j][1]):
            output.append(genre_list[j][0])

#output
#如果找的到該電影
if output != []:
    print(movie + ": " + ", ".join(output))
#如果找不到該電影
else:
    print("No movie found.")