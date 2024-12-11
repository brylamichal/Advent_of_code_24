import os
import numpy as np

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\06_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
ar = [line.strip() for line in lines]

input_lst = []
for row in ar:
    input_lst.append(np.array([s for s in row]))

ar = np.array(input_lst)
ar_02 = ar.copy()

print(ar)
print(ar.shape)

BOUNDARY = [ar.shape[0]-1, ar.shape[1]-1]


def check_boundary(idx):
    cond_row = 0 <= idx[0] <= BOUNDARY[0]
    cond_column = 0 <= idx[1] <= BOUNDARY[1]
    return cond_row and cond_column


def change_direction():
    global CURR_DIRECTION
    if CURR_DIRECTION == "up":
        CURR_DIRECTION = "right"
    elif CURR_DIRECTION == "right":
        CURR_DIRECTION = "down"
    elif CURR_DIRECTION == "down":
        CURR_DIRECTION = "left"
    else:
        CURR_DIRECTION = "up"


for index, val, in np.ndenumerate(ar):
    if val == "^":
        start_point = index

i = list(start_point)
ar[i[0]][i[1]] = "."
direction = {"up":      [-1, 0],
             "right":   [0, 1],
             "down":    [1, 0],
             "left":    [0, -1]}
CURR_DIRECTION = "up"
count = 0
while check_boundary(i):
    if ar[i[0]][i[1]] in [".", "X"]:
        ar[i[0]][i[1]] = "X"
        count += 1
        i[0] += direction[CURR_DIRECTION][0]
        i[1] += direction[CURR_DIRECTION][1]
    else:
        i[0] -= direction[CURR_DIRECTION][0]
        i[1] -= direction[CURR_DIRECTION][1]
        change_direction()
        i[0] += direction[CURR_DIRECTION][0]
        i[1] += direction[CURR_DIRECTION][1]


print(i)
print(count)

count_x = 0
for idx, val in np.ndenumerate(ar):
    if val == "X":
        count_x += 1

print(ar)
print(count_x)

dir_file_output = dir_name + '\\input\\06_day_output.txt'

#output = np.array2string(ar, separator='', max_line_width=np.inf, threshold=ar.size)
output = '\n'.join([''.join(row) for row in ar])
print(output)

# with open(dir_file_output, "a") as f:
#     f.write(output)


def change_local_direction(d):
    if d == "up":
        return "right"
    elif d == "right":
        return "down"
    elif d == "down":
        return "left"
    else:
        return "up"


i = list(start_point)
ar_02[i[0]][i[1]] = "."

CURR_DIRECTION_02 = "up"
count_O = 0
count_i = 0
while check_boundary(i):
    i[0] += direction[CURR_DIRECTION_02][0]
    i[1] += direction[CURR_DIRECTION_02][1]
    if not check_boundary(i):
        break
    if ar_02[i[0]][i[1]] == ".":
        j = i.copy()
        temp_ar_02 = ar_02.copy()
        temp_ar_02[j[0]][j[1]] = "#"
        j[0] -= direction[CURR_DIRECTION_02][0]
        j[1] -= direction[CURR_DIRECTION_02][1]
        temp_direction = change_local_direction(CURR_DIRECTION_02)
        j[0] += direction[temp_direction][0]
        j[1] += direction[temp_direction][1]
        iteration = 0
        while check_boundary(j):
            iteration += 1
            if iteration > 10**6:
                print(f"stop_iteration on idx {i}")
                count_i += 1
                break
            if j == [i[0]-direction[CURR_DIRECTION_02][0], i[1]-direction[CURR_DIRECTION_02][1]] and temp_direction == CURR_DIRECTION_02:
                count_O += 1
                break
            if temp_ar_02[j[0]][j[1]] == ".":
                j[0] += direction[temp_direction][0]
                j[1] += direction[temp_direction][1]
            else:
                j[0] -= direction[temp_direction][0]
                j[1] -= direction[temp_direction][1]
                temp_direction = change_local_direction(temp_direction)
                j[0] += direction[temp_direction][0]
                j[1] += direction[temp_direction][1]

    else:
        i[0] -= direction[CURR_DIRECTION_02][0]
        i[1] -= direction[CURR_DIRECTION_02][1]
        CURR_DIRECTION_02 = change_local_direction(CURR_DIRECTION_02)

print(count_O)
print(count_i)
print("done")

