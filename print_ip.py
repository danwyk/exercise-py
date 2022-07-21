# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

fhand = open("mbox-short.txt", 'r')
count = 0

line_list = fhand.readlines()
# print(line_list)

# for line in line_list:
#     if line.startswith("From "):
        
#         end_index = line.find(' ', 5)
#         # print(end_index)
#         line = line[5:end_index]
#         count += 1
#         print(line)


for line in line_list:
    if line.startswith("From "):
        word_list = line.split()
        print(word_list[1])
        count += 1

print(f"There were {count} lines in the file with From as the first word")
