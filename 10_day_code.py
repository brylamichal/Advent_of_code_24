import os
import numpy as np

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\10_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
ar = [line.strip() for line in lines]

input_lst = []
for row in ar:
    input_lst.append(np.array([int(s) for s in row]))

ar = np.array(input_lst)
print(ar)

BOUNDARY = [ar.shape[0]-1, ar.shape[1]-1]

direction = {"up":      [-1, 0],
             "right":   [0, 1],
             "down":    [1, 0],
             "left":    [0, -1]}

class Trailhead:
    def __init__(self, pos_0, main_ar):
        self.pos_0 = pos_0
        self.main_ar = main_ar
        self.achieved_top = []

        self.hike_top(pos=self.pos_0)
        self.score = len(set(tuple(el) for el in self.achieved_top))
    @staticmethod
    def check_boundary(pos):
        cond_row = 0 <= pos[0] <= BOUNDARY[0]
        cond_column = 0 <= pos[1] <= BOUNDARY[1]
        return cond_row and cond_column

    @staticmethod
    def move_up(pos):
        return [pos[0]-1, pos[1]+0]

    @staticmethod
    def move_down(pos):
        return [pos[0]+1, pos[1]+0]

    @staticmethod
    def move_right(pos):
        return [pos[0]+0, pos[1]+1]

    @staticmethod
    def move_left(pos):
        return [pos[0]+0, pos[1]-1]

    def hike_top(cls, pos):
        if cls.main_ar[pos[0]][pos[1]] == 9:
            cls.achieved_top.append(pos)
        else:
            if cls.check_boundary(cls.move_up(pos=pos)):
                copied_pos = cls.move_up(pos=pos.copy())
                if cls.main_ar[copied_pos[0]][copied_pos[1]] - cls.main_ar[pos[0]][pos[1]] == 1:
                    cls.hike_top(pos=copied_pos)

            if cls.check_boundary(cls.move_right(pos=pos)):
                copied_pos = cls.move_right(pos=pos.copy())
                if cls.main_ar[copied_pos[0]][copied_pos[1]] - cls.main_ar[pos[0]][pos[1]] == 1:
                    cls.hike_top(pos=copied_pos)

            if cls.check_boundary(cls.move_down(pos=pos)):
                copied_pos = cls.move_down(pos=pos.copy())
                if cls.main_ar[copied_pos[0]][copied_pos[1]] - cls.main_ar[pos[0]][pos[1]] == 1:
                    cls.hike_top(pos=copied_pos)

            if cls.check_boundary(cls.move_left(pos=pos)):
                copied_pos = cls.move_left(pos=pos.copy())
                if cls.main_ar[copied_pos[0]][copied_pos[1]] - cls.main_ar[pos[0]][pos[1]] == 1:
                    cls.hike_top(pos=copied_pos)


lst_Trailheads = []
for idx, val in np.ndenumerate(ar):
    if val == 0:
        lst_Trailheads.append(Trailhead(pos_0=list(idx), main_ar=ar))

answer = 0
for el in lst_Trailheads:
    answer += el.score

print(answer)

