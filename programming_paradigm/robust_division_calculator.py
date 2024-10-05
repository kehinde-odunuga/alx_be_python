
def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)
        result = x / y
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
# print(safe_divide(10, 2))   
# print(safe_divide(10, 0))
# print(safe_divide("ten", 2)) 