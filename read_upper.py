# Use words.txt as the file name
fname = input("Enter file name: ").lower()

# with open(fname, 'r') as fin:
#     words_list = fin.readlines()

fin = open(fname, 'r')
# words_list = fin.readlines()
words = fin.read()
print(words)
# for line in words_list:
#     print(line.strip().upper())

# for line in fin:
#     print(line.strip().upper())
