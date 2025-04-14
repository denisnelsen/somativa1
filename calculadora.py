from datetime import datetime

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("Calculadora")
    print("Operações disponíveis: +, -, *, /")
    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")

    if op == '+':
        resultado = somar(a, b)
    elif op == '-':
        resultado = subtrair(a, b)
    elif op == '*':
        resultado = multiplicar(a, b)
    elif op == '/':
        resultado = dividir(a, b)
    else:
        resultado = "Operação inválida!"

    print("Data e hora da operação:", datetime.now())
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()