keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

# turn strings into lists
keys = keys.split()
values = values.split()

# print the original string
combo = dict(zip(keys, values))

# print each word accoringly
print("English:", " ".join(keys))
print()
 
# print each word accordingly
for word in combo:
    print(word, "=", combo[word])

# print the trsanslated string
print()
print("Switdish:", " ".join(values))