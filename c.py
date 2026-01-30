import math

def complex_calculator():
    while True:
        try:
            calculation = input('Enter your calculation (e.g., sin(pi/2), 5*6): ').strip()

            # Replace any "math." expressions
            calculation = calculation.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
            calculation = calculation.replace("pi", "math.pi").replace("e", "math.e")

            # Evaluate the expression using eval (still risky if untrusted input is used)
            result = eval(calculation)
            print(f"Result: {result}")
        except (ValueError, SyntaxError) as e:
            print("Invalid input. Please enter a valid expression.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"Error: {e}")

complex_calculator()