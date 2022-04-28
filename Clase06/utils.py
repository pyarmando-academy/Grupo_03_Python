def calculadora(a, b, ope):
    if ope == "+":
        res = a + b
    elif ope == "-":
        res = a - b
    elif ope == "*":
        res = a * b
    elif ope == "/":
        res = a / b
    else:
        res = 0
    return res


def calcular_edad(año_actual, año_nac):
    edad = año_actual - año_nac
    return edad

