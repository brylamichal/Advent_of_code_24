import os
import re
import random
from itertools import chain, combinations, product

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\07_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
lines = [line.strip().split(":") for line in lines]
lines = [[int(line[0]), re.findall(r"\d+", line[1])] for line in lines]


def generate_comb(elems, n):
    return list(product(elems, repeat=n))

print(lines)

final_lst = []
for el in lines:
    ind = [int(i) for i in el[1]]
    res = el[0]
    combs = generate_comb(elems=[0, 1], n=len(ind))
    for comb in combs:
        temp_res = 0
        for i in range(len(comb)):
            if comb[i] == 0:
                temp_res += ind[i]
            else:
                temp_res *= ind[i]
        if temp_res == res:
            final_lst.append(res)
            break

print(sum(final_lst))

final_lst = []
for el in lines:
    ind = [int(i) for i in el[1]]
    res = el[0]
    combs = generate_comb(elems=[0, 1, 2], n=len(ind))
    # print(combs)
    for comb in combs:
        temp_res = 0
        for i in range(len(comb)):
            if comb[i] == 0:
                temp_res += ind[i]
            elif comb[i] == 1:
                temp_res *= ind[i]
            else:
                res_str = str(temp_res) + str(ind[i])
                temp_res = int(res_str)
        if temp_res == res:
            final_lst.append(res)
            break

print(sum(final_lst))





