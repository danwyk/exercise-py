# Method 1
# from ctypes.wintypes import PINT
# from logging.handlers import WatchedFileHandler


# Method 1
# --------------------------
# # set a serires of operation
# with open("friends.csv", 'r') as f:

#     # operation 1: print lines
#     for line in f:
#         # split string into temp_list
#         temp_list = line.strip().split(', ')

#         # print(temp_list)
#         print(f"In 2023, {temp_list[0]} will be {2030 - int(temp_list[1])} years old.")


# Method 2
# --------------------------
# open the file
file = open("friends.csv", 'r')
# line = file.readline()
# print(line)

# read each line and store it in outer_list
outer_list = file.readlines()
# print(outer_list)
# print("---------------------")

# print lines
for line in outer_list:  

    # line = line.strip().replace(',', '')

    # split string into a list
    line = line.strip().split(', ')

    # print line[0] and line[1]
    print(f"In 2023, {line[0]} will be {2030 - int(line[1])} years old.")
