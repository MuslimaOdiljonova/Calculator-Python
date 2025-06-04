def calculator(*args, **kwargs):
    user_input = input("Choose: addition, subtraction, multiplication, division: ").lower().strip()
    if user_input in kwargs:
        op = kwargs[user_input]
        try:
            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y
            }
            result = operations[op](a, b)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Cannot divide by 0!")
    else:
        print("Invalid!")
while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input! Enter only integers!")
calculator(a, b, addition = "+", subtraction = "-", multiplication = "*", division = "/")