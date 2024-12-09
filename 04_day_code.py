import os
### DAY 4 ##############################################################################################
import numpy as np

dir_name = os.path.dirname(__file__)
dir_file = dir_name + '\\input\\04_day_input.txt'

f = open(dir_file, "r")
lines = f.readlines()
ar = [line.strip() for line in lines]

# ar = ["MMMSXXMASM",
#       "MSAMXMSMSA",
#       "AMXSXMAAMM",
#       "MSAMASMSMX",
#       "XMASAMXAMM",
#       "XXAMMXXAMA",
#       "SMSMSASXSS",
#       "SAXAMASAAA",
#       "MAMMMXMMMM",
#       "MXMXAXMASX"]


input_lst = []
for row in ar:
      input_lst.append(np.array([s for s in row]))

ar = np.array(input_lst)

print(ar)
print(ar.shape)

# for x in np.nditer(ar):
#       print(x)

BOUNDARY = [ar.shape[0]-1, ar.shape[1]-1]


def check_boundary(idx):
      cond_row = 0 <= idx[0] <= BOUNDARY[0]
      cond_column = 0 <= idx[1] <= BOUNDARY[1]
      return cond_row and cond_column


def check_horizontal(ar, idx):
      local_count = 0
      temp_idx_pos = [idx[0]+3, idx[1]]
      if check_boundary(temp_idx_pos):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]+i, idx[1]]
            local_count += 1 if temp_str == "XMAS" else 0
      temp_idx_neg = [idx[0]-3, idx[1]]
      if check_boundary(temp_idx_neg):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]-i, idx[1]]
            local_count += 1 if temp_str == "XMAS" else 0
      return local_count

def check_vertical(ar, idx):
      local_count = 0
      temp_idx_pos = [idx[0], idx[1]+3]
      if check_boundary(temp_idx_pos):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0], idx[1]+i]
            local_count += 1 if temp_str == "XMAS" else 0
      temp_idx_neg = [idx[0], idx[1]-3]
      if check_boundary(temp_idx_neg):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0], idx[1]-i]
            local_count += 1 if temp_str == "XMAS" else 0
      return local_count


def check_diagonal(ar, idx):
      local_count = 0
      temp_idx_pos_pos = [idx[0]+3, idx[1]+3]
      if check_boundary(temp_idx_pos_pos):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]+i, idx[1]+i]
            local_count += 1 if temp_str == "XMAS" else 0
      temp_idx_neg_neg = [idx[0]-3, idx[1]-3]
      if check_boundary(temp_idx_neg_neg):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]-i, idx[1]-i]
            local_count += 1 if temp_str == "XMAS" else 0
      temp_idx_pos_neg = [idx[0]+3, idx[1]-3]
      if check_boundary(temp_idx_pos_neg):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]+i, idx[1]-i]
            local_count += 1 if temp_str == "XMAS" else 0
      temp_idx_neg_pos = [idx[0]-3, idx[1]+3]
      if check_boundary(temp_idx_neg_pos):
            temp_str = ""
            for i in range(4):
                  temp_str += ar[idx[0]-i, idx[1]+i]
            local_count += 1 if temp_str == "XMAS" else 0
      return local_count

count = 0
for index, val, in np.ndenumerate(ar):
      if val == "X":
         count += check_horizontal(ar=ar, idx=index)
         count += check_vertical(ar=ar, idx=index)
         count += check_diagonal(ar=ar, idx=index)

print(count)  # answer for first part


def check_boundary_X(idx):
      cond_row_1 = 0 <= idx[0] - 1 <= BOUNDARY[0]
      cond_row_2 = 0 <= idx[0] + 1 <= BOUNDARY[0]
      cond_column_1 = 0 <= idx[1] - 1 <= BOUNDARY[1]
      cond_column_2 = 0 <= idx[1] + 1 <= BOUNDARY[1]
      return all([cond_row_1, cond_row_2, cond_column_1, cond_column_2])

def check_diagonal_X(ar, idx):
      local_count = 0
      if check_boundary_X(idx=idx):
            temp_str_1 = ""
            for i in range(-1,2):
                  temp_str_1 += ar[idx[0]+i, idx[1]+i]
            cond1 = temp_str_1 == "MAS" or temp_str_1 == "SAM"
            temp_str_2 = ""
            for i in range(-1,2):
                  temp_str_2 += ar[idx[0]-i, idx[1]+i]
            cond2 = temp_str_2 == "MAS" or temp_str_2 == "SAM"
            local_count += 1 if all([cond1, cond2]) else 0
      return local_count

count = 0
for index, val, in np.ndenumerate(ar):
      if val == "A":
         count += check_diagonal_X(ar=ar, idx=index)

print(count)  # answer for second part
