# Create a Python script that asks user to enter a number
# Then use a for loop to print the multiplication table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
    result = number * num
    print(f"{number} * {num} = {result}")