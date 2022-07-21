# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fhand = open(fname)
# gross = 0.0
# count = 0

# for line in fhand:

#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue

#     target = float(line[line.find(' '):].strip())
#     gross += target
#     count += 1

# print(f"Average spam confidence: {gross / count}")

fruit = 'Banana'
fruit[0] = 'b'
# fruit = fruit.replace(fruit[0], 'b')
print(fruit)