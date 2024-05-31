menu = """

=========== B A N C O   D I O ===========

SELECIONE OPERAÇÃO:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação. Valor inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação. Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação. Valor do saque maior que o limite.")

        elif excedeu_saques:
            print("Falha na operação. Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1

        else:
            print("Falha na operação. O valor informado é inválido.")

    elif opcao == "3":
        print("\n=========== B A N C O   D I O ===========")
        print("\n-------------- EXTRATO --------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------------------------")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")