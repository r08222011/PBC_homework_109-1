from datetime import datetime

class Dog:

    def __init__(self, name, height, weight, adopted_date):
        # Dog 的基本資訊
        self.name = name
        self.height = height 
        self.weight = weight 
        self.adopted_date = adopted_date
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = adopted_date
        self.is_small_dog = self.check_if_small_dog()

    def check_if_small_dog(self):
		# 判斷是否為小型犬，回傳 boolean 值
        if self.height > 60 or self.weight > 30:
            return False
        else:
            return True

    def walk(self, walk_date): 
        # 更新累積灰塵量
        if self.is_small_dog:
            # 依據小型犬的灰塵累積效率更新累積灰塵量
            self.dust += 3
        else:
            # 依據大型犬的灰塵累積效率更新累積灰塵量
            self.dust += 2

        # 更新散步次數、最大散步間隔時間、最近散步日期
        self.walk_count += 1
        # 為datetime格式
        new_date_difference = (walk_date-self.last_walk_date).days
        if new_date_difference > self.longest_duration:
            self.longest_duration = new_date_difference
        self.last_walk_date = walk_date

    def bathe(self):
        # 更新累積灰塵量
        self.dust = 0

# 第一行input - 今日日期
today = input()
def date_transform(date):
    date = date.split("/")
    # 使用 datetime 模組
    return datetime(int(date[0]), int(date[1]), int(date[2]))
today = date_transform(today)

# 第二行input - 任務和寵物名字
task_name = input()
task, name = "", ""
if task_name[4] == "A":
    # 如果是 A 就會有名字
    task, name = task_name.split(",")
else:
    # 若不是 A，則只有 task
    task = task_name

# 剩下的input
information = []
while True:
    current_input = input()
    if current_input == "Done":
        break
    else:
        information.append(current_input)
information = [i.split("|") for i in information]

# 建立dog的dictionary
dog_dict = {}
for i in range(len(information)):
    # A：新增Dog
    if information[i][0] == "A":
        dog_dict[information[i][1]] = Dog(name = information[i][1],
                                          height = int(information[i][2]),
                                          weight = int(information[i][3]),
                                          adopted_date = date_transform(information[i][4])
                                          )
    # B：洗澡
    elif information[i][0] == "B":
        dog_dict[information[i][1]].bathe()
    # C：散步
    elif information[i][0] == "W":
        dog_dict[information[i][1]].walk(date_transform(information[i][2]))
    # D：換主人
    elif information[i][0] == "L":
        # 用不到直接刪除
        del dog_dict[information[i][1]]

def output(task, name = name, today = today):
    # 將dictionary的內容存取成list
    dog_list = list(dog_dict.items())

    if task == "TaskA":
        target = dog_dict[name]
    else:
        # 排序的依據
        def sort_key(x):
            # 若出現負號是為了從大排到小
            standard_key = (x[1].is_small_dog, -x[1].weight, -x[1].height, x[1].name)
            # B：頻率最低
            if task == "TaskB":
                return (x[1].walk_count/(today-x[1].adopted_date).days,) + standard_key
            # C：最長散步間隔
            elif task == "TaskC":
                return (-x[1].longest_duration,) + standard_key
            elif task == "TaskD":
            # D：最多灰塵
                return (-x[1].dust,) + standard_key
        dog_list.sort(key = sort_key)
        target = dog_list[0][1]

    print("%s,%d,%d,%d"%(target.name,target.height,target.weight,target.dust))

# 輸出結果
output(task, name, today)