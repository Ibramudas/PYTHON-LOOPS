print("Hi, WELCOME TO MY FIRST PYTHON PROJECT", end=" ")
print("Enter yes or no to continue")

y = input(": ").lower()

b = "yes"
c = "no"

if y == c:
    print("You chose to exit. Goodbye!")
else:
    if y == b:
        print("Welcome to armstrong ai!")
    else:
        print("Invalid input. Please enter yes or no.")

while True:
    try:
        x = int(input("Enter your first digit (1-9): "))
        if 1 <= x <= 9:
            print("Your first value is", x)
            break
        else:
            print("INVALID INPUT. Please enter a digit between 1 and 9.")
    except ValueError:
        print("INVALID INPUT. Please enter a number.")

while True:
    try:
        y = int(input("Enter your second digit (0-9): "))
        if 0 <= y <= 9:
            print("Your second value is", y)
            break
        else:
            print("INVALID INPUT. Please enter a digit between 0 and 9.")
    except ValueError:
        print("INVALID INPUT. Please enter a number.")

while True:
    try:
        z = int(input("Enter your third digit (0-9): "))
        if 0 <= z <= 9:
            print("Your third value is", z)
            break
        else:
            print("INVALID INPUT. Please enter a digit between 0 and 9.")
    except ValueError:
        print("INVALID INPUT. Please enter a number.")
print("Your 3 digits values are", x, y, z)

num = x**3 + y**3 + z**3
de = x*100 + y*10 + z

if num == de:
    print("Your 3 digits number is an Armstrong number")
else:
    print("Your 3 digits number is not an Armstrong number")
