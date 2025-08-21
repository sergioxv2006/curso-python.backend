num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /)")

print("----- RESULTADO -----")

match op:
    case '+':
        r = num1 + num2
        print("O Valor é: ", r)

    case '-':
        r = num1 - num2
        print("O Valor é: ", r)

    case '*':
        r = num1 * num2
        print("O Valor é: ", r)
        
    case '/':
        if num2 == 0:
            print("Erro: Não existe divisão por zero.")
        else:
            r = num1 / num2
            print("O Valor é: ", r)
    case _:
        print("Erro: Operação inválida.")