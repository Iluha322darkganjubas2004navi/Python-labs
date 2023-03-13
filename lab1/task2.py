def calc(num1, num2, operator):
    if(operator == "sum"):
        return [num1 + num2, num1, num2]
    if(operator == "sub"):
        return [num1 - num2, num1, num2]
    if (operator == "mult"):
        return [num1 * num2, num1, num2]
    if (operator == "div"):
        return [num1 / num2, num1, num2]
    else:
        return "Error!"