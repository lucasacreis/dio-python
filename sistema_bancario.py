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
        self.usuarios = {252525:1234, 424242:1123}
        self.contas = {'0001':252525, '0002': 424242}
        self.saldo = 0.0
        self.n_saque = 0
        self.n_transacoes_diarias = 0
        self.transacoes = {}
        self.Extrato = {'Saldo do dia': self.saldo, 'Transações': self.transacoes, 'Saldo Anterior': 0.0}
    

# Funções
# Limpar tela
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu 01
def menu1():
    menu = """
    ========== MENU ==========
    [u]\t Criar Usuário
    [q]\t Sair

    Entrar com CPF => """
    return input(textwrap.dedent(menu))

# Autenticação
def autenticacao(usuario):
    tentativa = 0
    while tentativa <= 3:
        senha = input("Digite sua senha => ")
        if senha != usuario:
            tentativa += 1
            print('\nSenha incorreta.')
        else:
            limpar()
            return True
        # END if
    # END While

    if tentativa == 3:
        print('Sua senha foi bloqueada, entre em contato com a sua agencia.')
    # END if
    
    return False


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
def deposito(saldo, valor, extrato, /):
    while True:
        if valor > 0:
            limpar()
            saldo += valor         # Atualiza o saldo
            # Atualiza o extrato
            extrato['Saldo do dia'] = saldo
            return saldo, extrato
        else:
            print('Valor inválido!')
            valor = float(input('Digite o valor do deposito: R$'))
        # END if
    # END While


# Saque
def saque(*, saldo, valor, extrato, limite, n_saque, limite_saques):
    print('Saque')
    if n_saque == limite_saques:
        print(f'Limite de 3 saques diários atingido!')
        wait = input('Pressione ENTER para retornar ao menu principal...')
        continue
    
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
        banco.saldo -= saque            # Atualiza o saldo
        banco.n_saque += 1              # Atualiza o número de saques diários
        banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
        # Atualiza o extrato
        banco.Extrato['Saldo do dia'] = banco.saldo
        # Atualiza Transações
        timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
        saque_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' -    SAQUE'
        banco.transacoes.update({saque_id: saque})
        print(f'Saldo atual: R${banco.saldo:.2f}')
        # Exibe mensagem de sucesso
        print(f'Saque de R${saque:.2f} realizado com sucesso!')
#   return saldo, extrato


# Extrato
def extrato():
    return


# Criar Usuário
def criar_usuario():
    return


# Filtrar Usuário
def filtrar_usuario():
    return


# Criar Conta
def criar_conta():
    return



# Função Principal
def main():
#    Cria uma instância da classe banco
    banco = Caixa()
    
    while True:
        while banco.menu == 1:
            limpar()
            """
            Exibe o Menu 01 e recebe opção do usuário.
            Menu 01:
            [u]\t Criar Usuário
            [q]\t Sair

            Entrar com CPF =>
            """
            opcao1 = menu1()

            if opcao1 == 'u':
                # Criar Novo Usuário
                cpf = criar_usuario()

            elif opcao1 == 'q':
                print('Saindo...')
                time.sleep(3)
                sys.exit(2)

            elif opcao1.isnumeric():
                limpar()
                usuario = self.usuarios[opcao1]
                autorizado = autenticacao(usuario)
                if autorizado is False:
                    print('Encerrando operações...')
                    time.sleep(3)
                    sys.exit(2)

                elif autorizado is True:
                    menu = 2
                # END if
            else:
                    print('Opção inválida!')
            # END if

        # END While
        while banco.menu == 1:
            opcao2 = menu2()

            # Caso número de transações diárias passar do limite estipulado
            if banco.n_transacoes_diarias == banco.LIMITE_TRANSACOES:
                print('Você atingiu seu limite diário de 10 transações.')
                print('Encerrando.')
                break
            else:
                if opcao2 == 'd':
                    limpar()
                    print('Deposito')
                    print(f'Valor disponível: R${banco.saldo:.2f}')
                    valor = float(input('Digite o valor do deposito: R$'))

                    banco.saldo, banco.extrato = deposito(banco.saldo, valor, banco.Extrato)
                    
                    banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                    timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
                    deposito_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' - DEPOSITO'
                    banco.transacoes.update({deposito_id: deposito})
                    print(f'Saldo atual: R${banco.saldo:.2f}')
                    # Exibe mensagem de sucesso
                    print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
                    wait = input('Pressione ENTER para retornar ao menu principal...')
                    limpar()
                else:
                    print('Opção inválida!')


"""
            # Verifica a opção escolhida
            if opcao == 's':
                limpar()
                # Chamar função saque
                print('Saque')
                if banco.n_saque == banco.LIMITE_SAQUE_DIARIO:
                    print(f'Limite de 3 saques diários atingido!')
                    wait = input('Pressione ENTER para retornar ao menu principal...')
                    continue
                
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
                    banco.saldo -= saque            # Atualiza o saldo
                    banco.n_saque += 1              # Atualiza o número de saques diários
                    banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                    # Atualiza o extrato
                    banco.Extrato['Saldo do dia'] = banco.saldo
                    # Atualiza Transações
                    timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
                    saque_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' -    SAQUE'
                    banco.transacoes.update({saque_id: saque})
                    print(f'Saldo atual: R${banco.saldo:.2f}')
                    # Exibe mensagem de sucesso
                    print(f'Saque de R${saque:.2f} realizado com sucesso!')
                wait = input('Pressione ENTER para retornar ao menu principal...')

            elif opcao == 'e':
                limpar()
                banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                print('Extrato')
                print('==============================================')
                print(f'Saldo Anterior:                   R${banco.Extrato["Saldo Anterior"]:>9.2f}')
                for key, value in banco.transacoes.items():
                    print(f'{key:<12}: R${value:>9.2f}')
                print(f'Saldo do dia {str(datetime.today().date())}:          R${banco.Extrato["Saldo do dia"]:>9.2f}')
                print('==============================================')
                wait = input('Pressione ENTER para retornar ao menu principal...')
            
            elif opcao == 'd':
                limpar()
                print('Deposito')
                print(f'Valor disponível: R${banco.saldo:.2f}')
                deposito = int(input('Digite o valor do deposito: R$'))
                if deposito <= 0:
                    print('Valor inválido!')
                else:
                    limpar()
                    banco.saldo += deposito         # Atualiza o saldo
                    banco.n_transacoes_diarias += 1 # Atualiza o número de transações diárias
                    # Atualiza o extrato
                    banco.Extrato['Saldo do dia'] = banco.saldo
                    # Atualiza Transações
                    timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))
                    deposito_id = str(timestamp.strftime('%d/%m/%Y - %H:%M:%S')) + ' - DEPOSITO'
                    banco.transacoes.update({deposito_id: deposito})
                    print(f'Saldo atual: R${banco.saldo:.2f}')
                    # Exibe mensagem de sucesso
                    print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
                    wait = input('Pressione ENTER para retornar ao menu principal...')
                    limpar()
                # END if

            elif opcao == 'q':
                print('Saindo...')
                sys.exit(2)
            else:
                print('Opção inválida!')
# END main
"""

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
