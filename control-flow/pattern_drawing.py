#  Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw Pattern
row = 0

while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
