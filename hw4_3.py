# inputs
input1 = input().split(",")
input2 = input().split(",")
input3 = input().split(",")

# turn into int
n, B  = int(input1[0]), int(input1[1])
w     = [int(input2[i]) for i in range(n)] # weight
v     = [int(input3[i]) for i in range(n)] # value
r     = [  v[i]/w[i]    for i in range(n)] # CP value

#---------- First Algorithm ------------

# sort the cp value
rsort = [  v[i]/w[i]    for i in range(n)] # sorted r
rsort.sort()
rsort.reverse()

weight_1     = 0  # total wight
efficiency_1 = 0  # total efficiency
x_1          = [] # output
for i in range(n):
    index = r.index(rsort[i]) # index of the item
    if weight_1 + w[index] <= B:
        weight_1     += w[index]
        efficiency_1 += v[index]
        x_1.append(index+1) # plus one since the initial index of item is 1
    if weight_1 == B:
        break

#---------- Second Algorithm ------------

vsort = [int(input3[i]) for i in range(n)] # sorted value
vsort.sort()
vsort.reverse()

weight_2     = 0  # total wight
efficiency_2 = 0  # total efficiency
x_2          = [] # output
for i in range(n):
    index = v.index(vsort[i]) # index of the item
    if weight_2 + w[index] <= B:
        weight_2     += w[index]
        efficiency_2 += v[index]
        x_2.append(index+1) # plus one since the initial index of item is 1
    if weight_2 == B:
        break

#------- Choose the best efficiency------

output = ""
if efficiency_1 >= efficiency_2:
    # sort x_1 and turn into string
    x_1.sort()
    for i in range(len(x_1)):
        output += str(x_1[i])
        if i != len(x_1) - 1:
            output += ","
else:
    # sort x_2 and turn into string
    x_2.sort()
    for i in range(len(x_2)):
        output += str(x_2[i])
        if i != len(x_2) - 1:
            output += ","

print(output)