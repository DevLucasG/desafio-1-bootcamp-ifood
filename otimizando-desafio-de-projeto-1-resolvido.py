import textwrap # codigo para identação na hora de imprimir na tela


def exibirMenu():
    menu = """"
    +------------------------------------+
    |   Escolha a opção desejada:        |
    |------------------------------------|
    |[d] Depositar...                    |
    |[s] Sacar...                        |
    |[e] Exibir Extrato...               |
    |[nu] Criar Usuário...               |
    |[nc] Criar Conta...                 |
    |[lc] Listar Contas...               |
    |[q] Sair...                         |
    +------------------------------------+
    ===>"""
    
    return input(textwrap.dedent(menu))
#
def depositar(saldo, valor, extrato, /): # passado por posição
    print("\n============== DEPOSITAR ================")
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n @@ Operação falhou! O valor informado é invalido. @@")
    print("\n=========================================")
    return saldo, extrato
#
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # passado por nome/argumento
    print("\n================== SACAR ==================")
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor de saque excedeu o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número maximo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    print("\n===========================================")

    return saldo, extrato
#
def exibir_extrato(saldo, /, *, extrato): # passados saldo por posição e extrato nomeado
    print("\n================== EXTRATO ==================")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n=============================================")
#
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@ Já existe usuário com esse CPF. @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data nascimento": data_nascimento, "cpf": cpf, "endereço": endereco}) # adicionando como dicionario

    print("=== Usuário criado com sucesso! ===")
#
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # retorna o usuario
                          # /\ ESSE usuario
    return usuarios_filtrados[0] if usuarios_filtrados else None # verificando se o " usuarios filtrados" é uma lista vazia
#
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # retorno o dicionario
    
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
#
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
#
def main():

    LIMITE_SAQUES = 3 # CONSTANTE
    AGENCIA = "0001" # CONSTANTE

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibirMenu()

        if opcao == "d":
            valor = float(input("Informe o valor do déposito: "))

            saldo, extrato = depositar(saldo, valor, extrato) # Função depositar retorna saldo e extrato

        elif opcao == "s":
            valor = float(input("Informe o valor para saque: "))

            saldo, extrato = sacar (
            
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta: # se a conta não retornar como "None", ela recebe o dicionario de conta e adiciona em contas
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
#

main()