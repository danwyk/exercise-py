fname = input("Enter file name: ")
fhand = open(fname, 'r')
original = fhand.read().split()
# print(original)


sorted = list()

for item in original:
    item = item.strip()
    # print(item)

    if item not in sorted:
        sorted.append(item)
sorted.sort()
print(sorted)