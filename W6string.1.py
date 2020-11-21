#
aname = input("Please enter your name:"):
print("Hello" ,aname)

#string 的 index
str1 = "MYPHONE"
str[0]
str[1]
str[-1] #抓倒數第一個字
str[-2]

#Slicing Strings 抓一小段文字出來
#syntax: <string>[<start>:<end>]
str1[3:5]
str1[2:6]
str1[2:] #傳回2開始的所有東西
str1[:5] #傳回5之前的所有東西

#Some String operations
a = "spam" + "eggs"
print(a)
b = 3 * "spam"
print(b)
c = "spam" * 5
print(c)
d = "spam" * 5 + "eggs" * 3
print(d)

#
a1 = "career"
for ch  in a1:
    print("Get a character:", ch)