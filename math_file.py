def equation(equation):
    try:
        return eval(equation)
    except ValueError:
        return print("Syntax Error")
    except ZeroDivisionError:
        return print("Can't divide by 0")