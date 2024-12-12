import os
import numpy as np

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\08_day_input.txt'

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


def set_hash(idx_ref, idx_del):
    dx = idx_ref[0] - idx_del[0]
    dy = idx_ref[1] - idx_del[1]
    return [idx_ref[0] + dx, idx_ref[1] + dy]


def check_boundary(idx):
    cond_row = 0 <= idx[0] <= BOUNDARY[0]
    cond_column = 0 <= idx[1] <= BOUNDARY[1]
    return cond_row and cond_column


def check_overlap(idx, key_to_skip, dict):
    for key in dict:
        if key == key_to_skip:
            continue
        elif idx in dict[key]:
            return True
    return False

anthens = {}
for idx, val in np.ndenumerate(ar):
    if val == ".":
        continue
    elif str(val) in anthens:
        anthens[str(val)].append(list(idx))
    else:
        anthens[str(val)] = [list(idx)]

print(anthens)

anthens_hash = {key:[] for key in anthens}
anthens_skipped = {key:[] for key in anthens}
for key in anthens:
    for i in range(len(anthens[key])):
        for j in range(len(anthens[key])):
            if i != j:
                idx_hash = set_hash(idx_ref=anthens[key][i], idx_del=anthens[key][j])
                cond = all([check_boundary(idx=idx_hash), not check_overlap(idx=idx_hash, key_to_skip=None, dict=anthens)])
                anthens_hash[key].append(idx_hash) if cond else anthens_skipped[key].append(idx_hash)

print("Anthens hashed:")
print(anthens_hash)
print("Anthens skipped:")
print(anthens_skipped)

count = 0
for key in anthens_hash:
    count += len(anthens_hash[key])

print(count) # 416 too high


