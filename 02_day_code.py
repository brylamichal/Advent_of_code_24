import os
# ## DAY 2 ############################################################################################

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\02_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
inital_lst = [x.split(' ') for x in lines]
input_lst = []

for l in inital_lst:
    input_lst.append([int(i) for i in l])

# input_lst = [[7, 6, 4, 2, 1],
#             [1, 2, 7, 8, 9],
#             [9, 7, 6, 2, 1],
#             [1, 3, 2, 4, 5],
#             [8, 6, 4, 4, 1],
#             [1, 3, 6, 7, 9]]


def check_safe(lst):
    if lst[0] > lst[1]:
        lst_bool = [(lst[i] > lst[i+1] and lst[i] - lst[i+1] < 4) for i in range(len(lst)-1)]
        return all(lst_bool)
    elif lst[0] < lst[1]:
        lst_bool = [lst[i] < lst[i+1] and lst[i+1] - lst[i] < 4 for i in range(len(lst)-1)]
        return all(lst_bool)
    else:
        return False


count = 0
i = 0
for el in input_lst:
    i += 1
    # print((i, check_safe(lst=el)))
    count += 1 if check_safe(lst=el) else 0

print(count)  # answer for first part
# print(input_lst)

count = 0
for el in input_lst:
    count += 1 if check_safe(lst=el) else 0
    if not check_safe(lst=el):
        lst_bool = []
        for i in range(len(el)):
            temp_lst = el.copy()
            temp_lst.pop(i)
            lst_bool.append(check_safe(temp_lst))
        count += 1 if any(lst_bool) else 0

print(count)  # answer for second part
