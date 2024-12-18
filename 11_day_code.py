import os
import sys
from functools import lru_cache

sys.setrecursionlimit(1000)

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\11_day_input.txt'

f = open(dir_file, "r")
line = f.readlines()[0].strip()
input_lst = line.split(" ")
print(input_lst)



class Stone:
    def __init__(self, number, blinks):
        self.number = number
        self.changed_stones = [self.number]
        self.blinks = blinks

        # self.iter_blinking(n=self.blinks)
        self.recurrence_blinking(n=self.blinks)
        self.count_stones = len(self.changed_stones)

    def rule_first(self):
        return "1"

    def rule_second(self, d):
        return [d[:(int(len(d)/2))], str(int(d[int((len(d)/2)):]))]

    def rule_third(self, d):
        return str(int(d) * 2024)

    def recurrence_blinking(cls, n):
        if n > 0:
            # print(f"{cls.number}:{n}")
            temp_lst = []
            for el in cls.changed_stones:
                if el == "0":
                    temp_lst.append(cls.rule_first())
                elif len(el) % 2 == 0:
                    temp_lst.append(cls.rule_second(d=el))
                else:
                    temp_lst.append(cls.rule_third(d=el))
            cls.changed_stones = [item for sublist in temp_lst for item in (sublist if isinstance(sublist, list) else [sublist])]
            cls.recurrence_blinking(n=n - 1)

    def iter_blinking(self, n):
        while n > 0:
            temp_lst = []
            for el in self.changed_stones:
                if el == "0":
                    temp_lst.append(self.rule_first())
                elif len(el) % 2 == 0:
                    temp_lst.append(self.rule_second(d=el))
                else:
                    temp_lst.append(self.rule_third(d=el))
            self.changed_stones = [item for sublist in temp_lst for item in (sublist if isinstance(sublist, list) else [sublist])]
            n -= 1


NUM_BLINKS = 4
lst_stones = []
for stone in input_lst:
    lst_stones.append(Stone(number=stone, blinks=NUM_BLINKS))

answer = 0
for stone in lst_stones:
    answer += stone.count_stones

print(answer)  # answer_part01 = 216042

stones = dict()

for stone in input_lst:
    stones[int(stone)] = 1

temp_stones = stones.copy()
blinks = 75
for i in range(blinks):
    for stone in stones:
        if stones[stone] == 0: continue
        else:
            if stone == 0:
                temp_stones[0] -= stones[stone]
                if 1 in temp_stones: temp_stones[1] += stones[stone]
                else: temp_stones[1] = stones[stone]
            elif len(str(stone)) % 2 == 0:
                mid = int(len(str(stone))/2)
                v1 = int(str(stone)[:mid])
                v2 = int(str(stone)[mid:])
                temp_stones[stone] -= stones[stone]
                if v1 in temp_stones: temp_stones[v1] += stones[stone]
                else: temp_stones[v1] = stones[stone]
                if v2 in temp_stones: temp_stones[v2] += stones[stone]
                else: temp_stones[v2] = stones[stone]
            else:
                v = stone * 2024
                temp_stones[stone] -= stones[stone]
                if v in temp_stones: temp_stones[v] += stones[stone]
                else: temp_stones[v] = stones[stone]

    stones = temp_stones.copy()

print(stones)

answer = 0
for count in stones.values():
    answer += count

print(answer)