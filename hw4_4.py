# inputs
input_1 = input().split(",")
input_2 = input().split(",")
input_3 = input().split(",")

# turn into int
n, B, eta = int(input_1[0]), int(input_1[1]), int(input_1[2])
w = [int(input_2[i]) for i in range(n)]
v = [int(input_3[i]) for i in range(n)]

# covariance matrix
covariance_matrix = []
# add matrix element
for i in range(n):
    matrix_row = input().split(",")
    matrix_row = [int(matrix_row[i]) for i in range(n)]
    covariance_matrix.append(matrix_row)

# compute
total_weight = 0  # total weight
total_value  = 0  # total value
indexs       = [] # index of item (start from 0)

while total_weight < B:
    current_best_index = -1
    current_best_value = total_value
    current_best_weight  = -1 # the higher the best
    for some_index in range(n):
        # check if item has been selected, also the weight can not be over B
        if (some_index not in indexs) and (total_weight + w[some_index] <= B):
            # compute the total value
            value = v[some_index] - eta*covariance_matrix[some_index][some_index]
            for index_i in indexs:
                # count v_i * x_i
                value += v[index_i]
                # count eta * sigma_ij * x_i * x_j
                value -= 2*eta*covariance_matrix[index_i][some_index] # notice 2 comes from sum over i and j
                for index_j in indexs:
                    value -= eta*covariance_matrix[index_i][index_j]
            # check if is the max
            if value > current_best_value:
                current_best_index    = some_index
                current_best_value    = value
                current_best_weight = w[some_index]
            # if the value are the same for two items
            if value == current_best_value and current_best_index != -1:
                if w[some_index] < current_best_weight:
                    current_best_index    = some_index
                    current_best_value    = value
                    current_best_weight = w[some_index]


    # if nothing selected
    if current_best_index == -1:
        break
    # if something is selected
    else:
        total_weight += w[current_best_index]
        indexs.append(current_best_index)
        total_value = current_best_value

# turn indexs into string
if len(indexs) == 0:
    print(0)
else:
    indexs.sort()
    output = ""
    for i in range(len(indexs)):
        output += str(indexs[i]+1) # plus 1 for starting from 1
        if i != len(indexs) - 1:
            output += ","
    print(output)