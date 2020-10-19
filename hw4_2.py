# inputs
input1 = input().split(",")
input2 = input().split(",")
input3 = input().split(",")

# turn into int
n, B  = int(input1[0]), int(input1[1])
w     = [int(input2[i]) for i in range(n)] # weight
v     = [int(input3[i]) for i in range(n)] # value
r     = [  v[i]/w[i]    for i in range(n)] # CP value

# sort the cp value
rsort = [  v[i]/w[i]    for i in range(n)] # sorted r
rsort.sort()
rsort.reverse()

weight = 0  # total wight
x      = [] # output
for i in range(n):
    index = r.index(rsort[i]) # index of the item
    if weight + w[index] <= B:
        weight += w[index]
        x.append(index+1) # plus one since the initial index of item is 1
    if weight == B:
        break

# sort the x
x.sort()

# turn x into string
output = ""
for i in range(len(x)):
    output += str(x[i])
    if i != len(x) - 1:
        output += ","

print(output)