num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")
print("5 - NOVO NÚMERO")
print("6 - SAIR")
operacao = int(input("Selecione uma operação: "))
while operacao >0 and operacao <=6:
    match operacao:
        case 1:
            resultado = num1+num2
            print(f"{num1} + {num2} = {resultado}")
            break
        case 2:
            resultado = num1-num2
            print(f"{num1} - {num2} = {resultado}")
            break
        case 3:
            resultado = num1*num2
            print(f"{num1} x {num2} = {resultado}")
            break
        case 4:
           resultado = num1/num2
           print(f"{num1} / {num2} = {resultado}")
           break

        case 5:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            operacao = int(input("Selecione uma operação: "))
            continue
        case 6:
            print("Saindo...")
            print("FIM")
            break


