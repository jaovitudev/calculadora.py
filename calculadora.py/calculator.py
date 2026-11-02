numero = float(input("Digite um número: "))
sinal = input("Digite um sinal matemático (+, -, *, /): ")
numero1 = float(input("Digite outro número: "))

def calculadora():
    if sinal == "+":
        return numero + numero1
    elif sinal == "-":
        return numero - numero1
    elif sinal == "*":
        return numero * numero1
    elif sinal == "/":
        if numero1 == 0:
            return "Não é possível dividir por zero."
        return numero / numero1
    else:
        return "Sinal inválido."

print(calculadora())
