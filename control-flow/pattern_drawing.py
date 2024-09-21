# Create a python script that prompts users to enter a positive integer
# Then use nested loops to print a square pattern of that size made of asterisks (*).

rows = int(input("Enter the size of the pattern: "))
i = 1

while i <= rows:
    j = 0
    for j in range(rows):
        print("*", end="")
        j += 1
    print()
    i += 1