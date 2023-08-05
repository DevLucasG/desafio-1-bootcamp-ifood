
def exibirMenu():
    menu = """"
    +------------------------------------+
    |   Escolha a opção desejada:        |
    |------------------------------------|
    |[U] Criar usuário....               |
    |                                    |
    |[C] Criar conta corrente.....       |
    |                                    |
    |[D] Depositar.....                  |
    |                                    |
    |[S] Sacar.....                      |
    |                                    |
    |[E] Extrato.....                    |
    |                                    |
    |[SS] Sair.....                      |
    +------------------------------------+
    """
    return menu
#

def sacar(*,saldo, extrato, limite, numero_saques):

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
            extrato.append("Saque no valor de: " + valor_saque)
            numero_saques += 1
            
            print(f"\nSaldo antes: R$ {saldo:.2f}")
            saldo -= valor_saque
            print(f"\nSaldo depois: R$ {saldo:.2f}")
        #   
    #
    return saldo, extrato
#
def deposito(saldo, /, *, extrato):

    valor_deposito = float(input("\nDigite o valor em que deseja depositar: "))

    if valor_deposito < 0:
        print("\nNão é possivel depositar valor negativo!")
    #
    else:
        saldo += valor_deposito
        print(f"\nDeposito efetuado!\nSeu saldo é de: {saldo}")
        extrato.append("Deposito de: " + valor_deposito)
    #
#
def extrato(saldo, /, extrato):
      
    print(extrato)
    print(f"\nSaldo final de: {saldo}")
#
def criar_usuario(usuarios):
    print("Bem vindo!\nSolicitados que informe corretamente as informações a seguir para a conclusão do cadastro.\n")

    cpf_usuario = input("Por gentileza, digite o numero de CPF: ")
    
    verifica = verificaExistente(cpf_usuario, usuarios)

    if verifica:
        print("Usuario com esse CPF já cadastrado!")
    #
    else:
        nome_usuario = input("Digite o nome completo do usuario: ")
        data_nasc_usuario = input("Informe a data de nascimento\n[EXEMPLO]: (00/00/00)\nInforme: ")
        endereco_usuario = input("Informe seu endereço.\n[EXEMPLO]: [nome da rua], [numero da casa], [bairro], [cidade]-[sigla estado]\nInforme: ")

        usuarios.append({"cpf_usuario":cpf_usuario, "nome_usuario":nome_usuario, "data_nasc_usuario":data_nasc_usuario, "endereco_usuario":endereco_usuario})

        print(usuarios)

        print(f"\nERRO! Usuario cadastrado com sucesso.")


#
def criar_conta_corrente(contas_corrente,usuarios,cont_contas):
    print("Bem vindo!\nSolicitados que informe corretamente as informações a seguir para a conclusão do cadastro.\n")
    cpf = input("Primeiro, informe o CPF para analisarmos se você possui um cadastro em nossos sistemas.\nInforme: ")
    verifica = verificaExistente(cpf, usuarios)

    if verifica:
        print("Perfeito, verificamos que voce já tem um cadastro!\n")

        contas_corrente.append({"numero_conta": cont_contas, "agencia": AGENCIA, "cpf_usuario":cpf})

        print(f"Conta criada. Num. da Conta: {cont_contas}, Agencia: {AGENCIA}, Portador: {cpf}")

        cont_contas += 1

    #
    else:
        print("Será necessario criar uma conta de usuario antes de criar uma conta corrente.")
    
#

def verificaExistente(cpf_usuario, usuarios):
    
    verifica_usuario = [usuario for usuario in usuarios if usuario["cpf_usuario"] == cpf_usuario]
    return verifica_usuario[0] if verifica_usuario else None
    #
#

LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
continua = 0
usuarios = []
contas_corrente = []
cont_contas = 0
extrato = []
opcao = ""
i = 0 # começando o i valendo 1 apenas para sair bonitinho no print os saques realizados
j =0  # começando o j valendo 1 apenas para sair bonitinho no print os saques realizados

while continua != 2:
    print(exibirMenu())
    opcao = input("==> ")
    opcao = opcao.upper()

    if opcao == 'D':
        print("\nDeposito...")
        deposito(saldo, extrato)
    #
    elif opcao == 'S':
        print("\nSacar...")
        sacar(saldo, extrato, limite, numero_saques)

    elif opcao == 'E':
        print("\nExtrato...")
        extrato(saldo, extrato )
    #
    elif opcao == 'U':
        print("\nCriar usuario...")
        criar_usuario(usuarios)
    #
    elif opcao == 'C':
        print("\nCriar conta corrente...")
        criar_conta_corrente(contas_corrente ,usuarios,cont_contas)
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