# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# generate and print the multiplication table


for y in range(1, 11):
    z = number * y
    print(f"{number} * {y} = {z}")
    