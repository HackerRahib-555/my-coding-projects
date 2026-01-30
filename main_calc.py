from math_file import equation

while True:
    user_input = input("Enter a math expression (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    result = equation(user_input)
    print("Result:", result)