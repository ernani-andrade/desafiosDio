menu = """Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
saques_feitos = 0


while True:

    opcao = input(menu)

    if opcao == "d":
        while True:
            deposito = float(input("Digite o valor do depósito (ou 0 para sair): "))
            if deposito == 0:
                break
            if deposito < 0:
                print("Valor inválido")
            else:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
           
    elif opcao == "s":
        if saques_feitos >= LIMITE_SAQUES:
            print("Limite de saques diários atingido")
        else:
            saque = float(input("Digite o valor do saque: "))
            if saque <= 0 or saque > limite or saque > saldo:
                print("Saque inválido")
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                saques_feitos += 1
                print("Saque realizado")

    elif opcao == "e":
        print("Extrato")
        print("Não foram feitas movimentações" if not extrato else extrato)
        print(f"\nSeu saldo atual é: R$ {saldo}")

    elif opcao == "q":
        break
    else:
        print("Selecione uma opção válida")