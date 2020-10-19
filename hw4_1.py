# inputs
input1 = input().split(",")
input2 = input().split(",")
input3 = input().split(",")
input4 = input().split(",")

# turn into int
n, B = int(input1[0]), int(input1[1])
w    = [int(input2[i]) for i in range(n)] # weight
v    = [int(input3[i]) for i in range(n)] # value
x    = [int(input4[i]) for i in range(n)] # bool

# check the x
weight     = 0 # total weight
efficiency = 0 # total efficiency
for i in range(n):
    if x[i] == 1:
        weight     += w[i]
        efficiency += v[i]

# if it is a valid solution
if weight <= B:
    #print total weight and total efficiency
    print(weight)
    print(efficiency)
else:
    print(-1)