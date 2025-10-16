import os
import sys
import time
from datetime import datetime
import pytz
import textwrap

class Caixa():
    def __init__(self):
        self.LIMITE_TRANSACOES = 10
        self.LIMITE_SAQUE_VALOR = 500.0
        self.LIMITE_SAQUE_DIARIO = 3
        self.menu = 1
        self.usuarios = {'25':123, '13':31}
        self.contas = {'0001':25, '0002': 13}
        self.saldo = 0.0
        self.n_saque = 0
        self.n_transacoes_diarias = 0
        self.transacoes = {}
        self.Extrato = {'Saldo do dia': self.saldo, 'Transações': self.transacoes, 'Saldo Anterior': 0.0}
    

# Funções
# Limpar tela
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


# Timer
def timer(t=3):
    for n in range(1,t):
        time.sleep(1)
        print('.', end=' ')


# Menu 01 e funções de usuários e contas
def menu1():
    menu = """
    ========== MENU ==========
    [u]\t Criar Usuário
    [q]\t Sair

    Entrar com CPF => """
    return input(textwrap.dedent(menu))

# Criar Usuário
def criar_usuario(usuarios):
    while True:
        limpar()
        print('===== Novo Usuário =====')
        print('Bem vindo ao Banco Heisu.')
        
        cpf = input('Digite seu CPF => ')
        if cpf.isnumeric():
            # Confere se usuário já é cadastrado
            usuario = None
            user = filtrar_usuario(cpf, usuarios)
            while user is False:
                senha = input('Digite sua senha => ')
                if senha.isnumeric():
                    usuario = {str(cpf): senha}
                    user = True
                    print('Usuário criado com sucesso!')
                else:
                    print('Use apenas números inteiros.\nTente novamente. ')
                    timer(2)
                    continue
                # END if
            # END while
            timer()
            break
        else:
            print('Use apenas números inteiros.\nTente novamente. ')
            timer(2)
            continue
        # END if

    return usuario


# Filtrar Usuário
def filtrar_usuario(cpf, usuarios):
    if usuarios.get(str(cpf)):
        print(f'Usuário {cpf} já existe.')
        return True
    else:
        return False
    

# Criar Conta
def criar_conta():
    return


# Autenticação
def autenticacao(usuario):
    tentativa = 1
    while tentativa <= 3:
        senha = str(input("Digite sua senha => "))
        if senha != str(usuario):
            tentativa += 1
            print('\nSenha incorreta.')
        else:
            limpar()
            return True
        # END if
    # END While
    print('Sua senha foi bloqueada, entre em contato com a sua agencia.')
    return False


# Menu 2 e funções bancárias
def menu2():
    menu = """
    ========== MENU ==========
    [s]\t Saque
    [e]\t Extrato
    [d]\t Deposito
    [c]\t Criar Conta
    [q]\t Sair
    => """
    return input(textwrap.dedent(menu))


# Deposito
def deposito(saldo, /):
    print('====== Depósito ======')
    print(f'Saldo atual: R${saldo:.2f}')
    valor = float(input('Digite o valor do deposito: R$'))
    while True:
        if valor >= 0:
            limpar()
            return valor
        else:
            print('Valor inválido!')
            valor = float(input('Digite o valor do deposito: R$'))
        # END if
    # END While


# Saque
def saque(*, n_saque, saldo, LIMITE_SAQUE_DIARIO, LIMITE_SAQUE_VALOR):
    print('======= Saque =======')
    print(f'Saldo atual: R${saldo:.2f}')
    
    if n_saque == LIMITE_SAQUE_DIARIO:
            print(f'Limite de 3 saques diários atingido!')
            input('Pressione ENTER para retornar ao menu principal...')
            return 0

    while True:
        valor = float(input('Digite o valor do saque: R$'))

        if valor > LIMITE_SAQUE_VALOR:
            print(f'Valor acima do permitido para saque! Limite máximo: R${LIMITE_SAQUE_VALOR:.2f}')
        elif valor > saldo:
            print('Saldo insuficiente!')
        elif valor < 0:
            print('Valor inválido!')
        else:
            limpar()
            return valor
        # END if
    # END While

    '''print('Saque')
    if n_saque == limite_saques:
        print(f'Limite de 3 saques diários atingido!')
        wait = input('Pressione ENTER para retornar ao menu principal...')
    
    print(f'Valor disponível: R${banco.saldo:.2f}')
    saque = int(input('Digite o valor do saque: R$'))
    if saque > banco.LIMITE_SAQUE_VALOR:
        print(f'Valor acima do permitido para saque! Limite máximo: R${banco.LIMITE_SAQUE_VALOR:.2f}')
    elif saque <= 0:
        print('Valor inválido!')
    elif saque > banco.saldo:
        print('Saldo insuficiente!')
    else:
        limpar()
        saldo -= saque            # Atualiza o saldo
        n_saque += 1              # Atualiza o número de saques diários
        n_transacoes_diarias += 1 # Atualiza o número de transações diárias
        # Atualiza o extrato
        Extrato['Saldo do dia'] = banco.saldo
        # Atualiza Transações
        timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
        saque_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' -    SAQUE'
        banco.transacoes.update({saque_id: saque})
        print(f'Saldo atual: R${banco.saldo:.2f}')
        # Exibe mensagem de sucesso
        print(f'Saque de R${saque:.2f} realizado com sucesso!')
#   return saldo, extrato'''


# Exibir Extrato
def extrato(Extrato, transacoes):
    limpar()
    print('=================== Extrato ==================')
    print('==============================================')
    print(f'Saldo Anterior:                   R${Extrato["Saldo Anterior"]:>9.2f}')
    for key, value in transacoes.items():
        print(f'{key:<12}: R${value:>9.2f}')
    print(f'Saldo do dia {str(datetime.today().date())}:          R${Extrato["Saldo do dia"]:>9.2f}')
    print('==============================================')
    return


#  Atualizar Extrato
def atualiza(opcao2, valor):
    timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
    if opcao2 == 'd':
        deposito_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' - DEPOSITO'
        transacao = {deposito_id: valor}
    elif opcao2 == 's':
        saque_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' -    SAQUE'
        transacao = {saque_id: valor}
    return transacao


# Função Principal
def main():
#    Cria uma instância da classe banco
    banco = Caixa()
    
    while True:
        # MENU 01 - Criação e Autenticação de Usuários
        while banco.menu == 1:
            limpar()
            """
            Chamada do Menu 1:
            [u]\t Criar Usuário
            [q]\t Sair
            Entrar com CPF =>
            """
            opcao1 = menu1()

            if opcao1 == 'u':
                # Criar Novo Usuário
                usuario = criar_usuario(banco.usuarios)
                if usuario is not None:
                    banco.usuarios.update(usuario)
                    print(banco.usuarios)

            elif opcao1 == 'q':
                print('Saindo', end='')
                timer()
                sys.exit(2)

            elif opcao1.isnumeric():
                limpar()
                usuario = banco.usuarios.get(str(opcao1))
                autorizado = autenticacao(usuario)
                print(f'Usuário {opcao1} autorizado. ')
                timer(2)

                if autorizado is False:
                    print('Encerrando operações.', end=' ')
                    timer()
                    sys.exit(2)

                elif autorizado is True:
                    banco.menu = 2
                # END if
            else:
                    print('Opção inválida!\nTente novamente. ')
                    timer(2)
            # END if
        # END While

        # MENU 02 - Transições Bancárias
        while banco.menu == 2:
            opcao2 = menu2()

            # Caso número de transações diárias passar do limite estipulado
            if banco.n_transacoes_diarias == banco.LIMITE_TRANSACOES:
                print('Você atingiu seu limite diário de 10 transações.')
                print('Encerrando.')
                break
            else:
                if opcao2 == 'd':
                    valor = deposito(banco.saldo)
                    if valor != 0:
                        banco.saldo += valor
                        banco.Extrato['Saldo do dia'] = banco.saldo
                        transacao = atualiza(opcao2, valor)
                        banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                        banco.transacoes.update(transacao)
                        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
                        print(f'Saldo atual: R${banco.saldo:.2f}')
                    else:
                        print('Valor de depósito nulo.')
                    # END if                    
                    input('Pressione ENTER para retornar ao menu principal...')
                    limpar()

                elif opcao2 == 's':
                    valor = saque(n_saque=banco.n_saque, 
                                  saldo=banco.saldo, 
                                  LIMITE_SAQUE_DIARIO=banco.LIMITE_SAQUE_DIARIO, 
                                  LIMITE_SAQUE_VALOR=banco.LIMITE_SAQUE_VALOR)                    
                    if valor != 0:
                        banco.saldo -= valor
                        banco.Extrato['Saldo do dia'] = banco.saldo
                        banco.n_saque += 1              # Atualiza o número de saques diários
                        transacao = atualiza(opcao2, valor)
                        banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                        banco.transacoes.update(transacao)
                        print(f'Saque de R${valor:.2f} realizado com sucesso!')
                        print(f'Saldo atual: R${banco.saldo:.2f}')
                        input('Pressione ENTER para retornar ao menu principal...')
                    else:
                        print('Valor de saque nulo.')
                    # END if                    
                    
                    limpar()

                elif opcao2 == 'e':
                    extrato(banco.Extrato, banco.transacoes)
                                     
                    input('Pressione ENTER para retornar ao menu principal...')
                    limpar()

                elif opcao2 == 'q':
                    print('Saindo', end='')
                    timer()
                    sys.exit(2)
                else:
                    print('Opção inválida!')


#######################
##### INICIO AQUI #####
#######################
if __name__ == "__main__":
    # Executa a rotina principal
    try:
        # Chama a função main
        main()
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo teclado!')
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
    except SystemExit:
        print('Programa interrompido!')
        try:
            sys.exit(2)
        except SystemExit:
            os._exit(2)
# END
