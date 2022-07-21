largest = None
smallest = None
first_time = True

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue;
    
    if first_time:
        largest = num
        smallest = num
        first_time = False

    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
        
print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")
