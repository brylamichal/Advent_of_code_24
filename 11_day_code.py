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

    @staticmethod
    def rule_first():
        return "1"

    @staticmethod
    def rule_second(d):
        return [d[:(int(len(d)/2))], str(int(d[int((len(d)/2)):]))]

    @staticmethod
    def rule_third(d):
        return str(int(d) * 2024)

    def recurrence_blinking(cls, n):
        if n > 0:
            print(f"{cls.number}:{n}")
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


# NUM_BLINKS = 25
# lst_stones = []
# for stone in input_lst:
#     lst_stones.append(Stone(number=stone, blinks=NUM_BLINKS))
#
# answer = 0
# for stone in lst_stones:
#     answer += stone.count_stones
#
# print(answer)  # answer_part01 = 216042

from collections import defaultdict

stones = defaultdict(int)

print(stones)

for stone in input_lst:
    stones[int(stone)] += 1



print(stones)
