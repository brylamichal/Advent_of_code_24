import os

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\05_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

temp_order_rule = []
temp_order_print = []
change = False
for line in lines:
    if line == "":
        change = True
        continue
    if change:
        temp_order_print.append(line)
    else:
        temp_order_rule.append(line)

order_rule = []
for x in temp_order_rule:
    temp_lst = x.split("|")
    order_rule.append([int(i) for i in temp_lst])

order_print = []
for x in temp_order_print:
    temp_lst = x.split(",")
    order_print.append([int(i) for i in temp_lst])

print(order_print)  # list from first task
print(order_rule)

d = {}
for el in order_rule:
    if str(el[0]) in d:
        d[str(el[0])].append(el[1])
    else:
        d[str(el[0])] = [el[1]]

print(d)


def check_rule(print_lst):
    add = False
    length = len(print_lst)
    for i, page in enumerate(print_lst):
        if i == (length - 1):
            continue
        elif not str(page) in d:
            return [False, i]
        else:
            temp_lst = []
            for j in range(i + 1, length):
                temp_lst.append(print_lst[j] in d[str(page)])
            if all(temp_lst):
                add = True
            else:
                return [False, i]
    return [add, None]


final_lst = []
second_part_lst = []
for print_lst in order_print:
    if check_rule(print_lst)[0]:
        final_lst.append(print_lst)
    else:
        second_part_lst.append(print_lst)

print(final_lst)

result = 0
for l in final_lst:
    result += l[int((len(l)-1)/2)]

print(result)  # answer for first part

print(second_part_lst)

correct_lst = []
for l in second_part_lst:
    while not check_rule(l)[0]:
        new_lst = l.copy()
        idx = check_rule(l)[1]
        new_lst.append(l[idx])
        new_lst.pop(idx)
        l = new_lst
    correct_lst.append(l)

print(correct_lst)

result_sorted = 0
for l in correct_lst:
    result_sorted += l[int((len(l)-1)/2)]

print(result_sorted)  # answer for the second part
