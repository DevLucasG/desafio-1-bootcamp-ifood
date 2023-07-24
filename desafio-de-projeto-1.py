## Desafio 1

# Criar um sistema bancario com as funções:
# depositar, sacar, extrato



menu = """"
+-------------------------------+
|   Escolha a opção desejada:   |
|                               |
|[D] Depositar.....             |
|                               |
|[S] Sacar.....                 |
|                               |
|[E] Extrato.....               |
|                               |
|[SS] Sair.....                 |
+-------------------------------+
"""

LIMITE_SAQUES = 3
saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
continua = 0
saques_realizados = []
depositos_realizados = []
opcao = ""
i = 0 # começando o i valendo 1 apenas para sair bonitinho no print os saques realizados
j =0  # começando o j valendo 1 apenas para sair bonitinho no print os saques realizados

while continua != 2:
    print(menu)
    opcao = input("==> ")
    opcao = opcao.upper()

    if opcao == 'D':
        print("\nDeposito...")

        valor_deposito = float(input("\nDigite o valor em que deseja depositar: "))

        if valor_deposito < 0:
            print("\nNão é possivel depositar valor negativo!")
        #
        else:
            saldo += valor_deposito
            print(f"\nDeposito efetuado!\nSeu saldo é de: {saldo}")
            depositos_realizados.append(valor_deposito)
        #
    #
    elif opcao == 'S':
        print("\nSacar...")

        if numero_saques >= LIMITE_SAQUES:
            print("\nO limite diario de saques já foi atingido! Tente novamente amanhã.")
        #
        else:
            valor_saque = float(input("\nDigite o valor para saque: "))

            if valor_saque > saldo:
                print("Saldo indisponivel!")                
            #

            elif valor_saque > limite:
                print("\nLimite atingido! O limite para saque é de R$ 500.00")
            #
            else:
                print("\nEfetuando o saque...")
                saques_realizados.append(valor_saque)
                numero_saques += 1
                
                print(f"\nSaldo antes: R$ {saldo:.2f}")
                saldo -= valor_saque
                print(f"\nSaldo depois: R$ {saldo:.2f}")
            #
        #   
    #
    elif opcao == 'E':
        print("\nExtrato...")

        for depositos in depositos_realizados:
            print(f"[Depositos {i+1}]: R$ {depositos_realizados[i]}")
            i+= 1
        # 
        print()
        for saques in saques_realizados:
            print(f"[Saques {i+1}]: R$ {saques_realizados[j]}")
            j+= 1
        # 
        print()
        print(f"[Saldo atual] R$ {saldo:.2f}")
    #

    elif opcao == 'SS':
        print("\nSaindo...")
        break
    #
    else:
        print("\nOpção invalida.")
        break 
    #

    continua = int(input("\nDeseja fazer uma nova operação?\n[1] Sim\n[2] Não\n==> "))
#