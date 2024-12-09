import os

# #### DAY 1 ###############################################################################################


dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\01_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
lst_1 = [int(x.split('   ')[0]) for x in lines]
lst_2 = [int(x.split('   ')[1]) for x in lines]

l1 = [3, 4, 2, 1, 3, 3]
l2 = [4, 3, 5, 3, 9, 3]

l1_sort = sorted(lst_1)
l2_sort = sorted(lst_2)

# my code
distance = 0

for i in range(len(l1_sort)):
    delta = abs(l2_sort[i] - l1_sort[i])
    distance += delta

print(distance)  # answer for first part
# print(l1_sort)
# print(l2_sort)


total_distance = sum(abs(b - a) for a, b in zip(l1_sort, l2_sort))
print(total_distance)  # answer for first part

####

total_sum = 0

for i in range(len(lst_1)):
    x = lst_1[i] * lst_2.count(lst_1[i])
    total_sum += x

print(total_sum)  # answer for second part
