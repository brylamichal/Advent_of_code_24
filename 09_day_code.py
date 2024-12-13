import os

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\09_day_input.txt'

f = open(dir_file, "r")
line = f.readlines()[1].strip()
print(line)


def change_individual_block(disk_map):
    res = []
    id = 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            res.extend([str(id) for i in range(int(disk_map[i]))])
            id += 1
        else:
            res.extend(["." for i in range(int(disk_map[i]))])
    return res


def check_rule(e):
    x = e.index(".")
    for i in range(x, len(e)):
        if e[i] == ".":
            continue
        else:
            return False
    return True


def move_file_blocks(individual_block):
    reserve_lst = individual_block[::-1]
    for i, el in enumerate(reserve_lst):
        if el == ".":
            continue
        elif check_rule(e=individual_block):
            break
        else:
            individual_block[individual_block.index(".")] = el
            individual_block[-1-i] = "."
    return individual_block


ind_blck = change_individual_block(disk_map=line)
print(ind_blck)
result_blck = move_file_blocks(individual_block=ind_blck.copy())
print(result_blck)

result = 0
for i, res in enumerate(result_blck):
    if res == ".":
        break
    else:
        result += i * int(res)

print(result)

def segregate_elems(lst):
    res_lst = []
    temp_lst = []
    for i in range(len(lst)):
        if i == 0:
            temp_lst.append(lst[i])
        elif lst[i] == lst[i-1]:
            temp_lst.append(lst[i])
        else:
            res_lst.append(temp_lst)
            temp_lst = [lst[i]]
        if i == len(lst) - 1:
            res_lst.append(temp_lst)
    return res_lst

print(segregate_elems(lst=ind_blck))


def move_whole_files_blocks(individual_block):
    run = True
    reserve_lst = segregate_elems(individual_block[::-1])
    for el in individual_block:
        if el == ".":
            continue
        else:
            first_elem = el
            break
    lst_moved = []
    while run:
        for j, res_el in enumerate(reserve_lst):
            if first_elem in res_el:
                run = False
                break
            elif "." in res_el:
                continue
            elif res_el in lst_moved:
                continue
            else:
                done_sth = False
                for i, el in enumerate(reserve_lst[::-1]):
                    if i > len(reserve_lst) - j - 1:
                        break
                    if not "." in el:
                        continue
                    elif len(res_el) == len(el):
                        reserve_lst[j] = el
                        reserve_lst[-1 - i] = res_el
                        done_sth = True
                        lst_moved.append(res_el)
                        break
                    elif len(res_el) < len(el):
                        reserve_lst[-1 - i] = res_el
                        reserve_lst.insert(-1 - i, ["."] * (len(el) - len(res_el)))
                        reserve_lst[j] = ["."] * len(res_el)
                        done_sth = True
                        lst_moved.append(res_el)
                        break
            if done_sth:
                break

    return [item for sublist in reserve_lst[::-1] for item in sublist]


print(move_whole_files_blocks(individual_block=ind_blck.copy()))
result_blck_p2 = move_whole_files_blocks(individual_block=ind_blck.copy())
result_p2 = 0
for i, res in enumerate(result_blck_p2):
    if res == ".":
        continue
    else:
        result_p2 += i * int(res)

print(result_p2)
