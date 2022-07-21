fhand = open("mbox-short.txt", 'r')

line_list = fhand.readlines()
frequency = dict()

for line in line_list:
    if line.startswith("From "):
        word_list = line.split()
        frequency[word_list[1]] = frequency.get(word_list[1], 0) + 1

max_val = max(frequency.values())

for item in frequency:
    if frequency[item] == max_val:
        max_key = item

print(max_key, max_val)
# print(frequency.values())

frequency.sort(key = lambda key: frequency[key])

