#input
n= 0
linelist = []
list_ = []

#input
for i in range(100):
    temp = input()
    if temp != "LINESTOP": #如果input不是"LINESTOP"就繼續讀入input資料
        temp = temp.split(",") 
        for j in range(4): #每次都是4個數字
            temp[j] = float(temp[j]) #將清單中的字串轉為浮點數
        linelist.append(temp) #將清單加入linelist
    elif temp == "LINESTOP": #如果input是"LINESTOP"就break
        break

#讀入位移
shift = input().split(",")


#移動圖形
def plotshift(linelist=linelist, xshift=0, yshift=0):
    for i in range(len(linelist)):
        for j in range(4):
            if j == 0 or j == 2: # x-coord. 
                linelist[i][j] += xshift #x座標移動
            else: # y-coord.
                linelist[i][j] += yshift #y座標移動

plotshift(linelist, float(shift[0]), float(shift[1])) #給定input

#做output函數
def printlines():
    for i in range(len(linelist)):
        print("Line%d: %.3f %.3f %.3f %.3f"%(i, linelist[i][0], linelist[i][1], linelist[i][2],linelist[i][3])) #取到小數點三位

#output
printlines()