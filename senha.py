senha = 1010
tentativa = 0
novaChance = 0
while tentativa != senha:
    tentativa = int(input("Digite sua senha: ",))
    novaChance +=1
    if  tentativa == senha:
        print("Login concluído")
        break
    else:
        print(f"Senha incorreta. essa foi sua chance {novaChance}")
    if novaChance == 2:
        print("Se errar mais uma vez, a senha será bloqueada.")
    elif novaChance == 3:
        print("Senha bloqueada!!!")
        break

