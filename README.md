# //////////////////////////////////////////////////////////////////////////////////////////
####################### OBSERVAÇÕES ####################### 

# Arquivo: otimizando-desafio-de-projeto-1
    
    # Foi a minha tentativa de resolver o projeto, tive bastante dificuldades em relações a parametros
    # pois venho com uma bagagem da linguagem C. O programa roda, porém não consegui implementar algumas das funcionalidades
    # que eu queria. Por isso, resolvi criar o arquivo "otimizando-desafio-de-projeto-1-resolvido" que ai eu fui acompanhando
    # a explicação da resolução para conseguir concluir.

# Arquivo: otimizando-desafio-de-projeto-1-resolvido

    # Acompanhando a resolução do desafio
    
# //////////////////////////////////////////////////////////////////////////////////////////



####################### Desafio 1 #######################
# OBJETIVO: -- 1º versão --

    # Criar um sistema bancario com as funções:
    # depositar, sacar, extrato

####################### Otimitando Desafio 1 ####################### 
# OBJETIVO: -- 2º versão --

    # Separar em funções: saque, deposito e extrato
    # Criar novas duas funções: cadastrar usuário(cliente) e cadastrar conta bancária

    # Instruções adicionais:

    # -- FUNÇÃO SAQUE:
        # função de saque deve receber os argumentos apenas por nome (keyword only),
        # SUGESTÃO DE ARGUMENTOS: saldo, valor, extrato, limite, numero_saques, limite_saques,
        # SUGESTÃO DE RETORNO: saldo e extrato.

    # -- FUNÇÃO DEPÓSITO:
        # função deve receber os argumentos apenas por posição (positional only)
        # SUGESTÃO DE ARGUMENTOS: saldo, valor, extrato,
        # SUGESTÃO DE RETORNO: saldo e extrato.

    # -- FUNÇÃO EXTRATO:
        # função deve receber os argumentos por posição e nome (positional only e keyword only)
        # ARGUMENTOS POSICIONAIS: saldo,
        # ARGUMENTOS NOMEADOS: extrato.

    # -- FUNÇÃO CRIAR USUÁRIO:
        # o programa deve armezenar os usuarios em uma lista,
        # é composto por: nome, data nasc, cpf e endereço.
        # string endereço = (logradouro, nro, bairro, cidade/sigla estado)
        # deve ser armazenado somente os números do CPF
        # não será possivel cadastrar usuarios com o mesmo CPF

    # -- FUNÇÃO CRIAR CONTA CORRENTE:
        # o programa deve armazenar as contas em uma lista,
        # é composta por: agencia, numero da conta e usuario,
        # o numero da conta é sequencial, iniciando em 1
        # o numero da agencia é fixo: "0001"
        # o usuario pode ter mais de uma conta, mas uma conta pertence apenas a um usuario


