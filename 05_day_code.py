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

print(order_print)
print(order_rule)
