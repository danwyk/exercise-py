# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
fhand = open("mbox-short.txt", 'r')

line_list = fhand.readlines()
frequency = dict()

for line in line_list:
    if line.startswith("From "):
        end_index = line.find(':')
        line = line[end_index - 2: end_index]
        frequency[line] = frequency.get(line, 0) + 1

for key in sorted(list(frequency)):
    print(key, frequency[key])



