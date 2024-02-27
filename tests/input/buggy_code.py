# This code snippet is intentionally buggy for demonstration purposes.


def calculate_sum(lst):
    # Intentional bug: sum is a built-in function, should not be used as variable name
    sum = 0
    for i in lst:
        # Intentional bug: 'i' is a string, cannot be added to an integer
        sum += i
    return sum


def divide(x, y):
    # Intentional bug: Division by zero is not handled
    return x / y


# Intentional bug: misspelled 'True' as 'Ture'
while Ture:
    print("This loop will run forever because of a typo")

# Intentional bug: 'calculate_sum' expects a list, not separate arguments
result = calculate_sum(1, 2, 3, 4)

# Intentional bug: 'divide' function may raise ZeroDivisionError
print(divide(10, 0))
