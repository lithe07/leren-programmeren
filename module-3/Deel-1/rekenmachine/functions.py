def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return  num1 / num2


def taak_uitvoeren(keuze, num1, num2):
    if keuze == "A":       
        return addition(num1, num2)
    elif keuze == "B":
        return  subtraction(num1, num2)
    elif keuze == "C":
        return multiplication(num1, num2)
    elif keuze == "D":
        return division(num1, num2)
    elif keuze == "E":
        return addition(num1, 1)
    elif keuze ==  "F":
        return subtraction(num1, 1)
    elif keuze == "G":
        return multiplication(num1, 2)
    elif keuze == "H":
        return division(num1, 2)
    

    

     


