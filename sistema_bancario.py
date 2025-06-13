import os
import sys
from datetime import datetime
import pytz

class Cliente():
    def __init__(self):
        self.MENU = """[s] Saque\n[e] Extrato\n[d] Deposito\n[q] Sair"""
        self.USER = 'Lucas'
        self.SENHA = int(112358)
        self.LIMITE_TRANSACOES = 10
        self.LIMITE_SAQUE_VALOR = 500.0
        self.LIMITE_SAQUE_DIARIO = 3
        self.saldo = 0.0
        self.n_saque = 0
        self.n_transacoes_diarias = 0
        self.transacoes = {}
        self.Extrato = {'Saldo do dia': self.saldo, 'Transações': self.transacoes, 'Saldo Anterior': 0.0}

    def run(self):
        self.limpar()
        user = 'Lucas' # str(input('Bem vindo ao Banco Reis!\nDigite o seu nome: > '))
        tentativa = 0
        if user.upper() != self.USER.upper():
            print('Usuário não cadastrado.')
            sys.exit(1)

        while tentativa <= 3:
            senha = 112358 # int(input('Digite sua senha: > '))

            if senha != self.SENHA:
                tentativa += 1
                print('\nSenha incorreta.')
            else:
                self.limpar()
                print(f'Bem vindo, {self.USER}')
                break
            # END if

        # END While
        
        if tentativa == 3:
            print('Sua senha foi bloqueada, entre em contato com a sua agencia.')
        # END if
    

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    #

def main():
#    Cria uma instância da classe banco
    banco = Cliente()

    while True:

        if banco.n_transacoes_diarias == banco.LIMITE_TRANSACOES:
            print('Você atingiu seu limite diário de 10 transações.')
            print('Encerrando.')
            break
        else:
            # Executa o método run da classe banco
            banco.run()
            # Exibe o menu
            print(banco.MENU)
            # Lê a opção do usuário
            opcao = input('Escolha uma opção: ')
            # Verifica a opção escolhida
            if opcao == 's':
                banco.limpar()
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
                    banco.limpar()
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
                banco.limpar()
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
                banco.limpar()
                print('Deposito')
                print(f'Valor disponível: R${banco.saldo:.2f}')
                deposito = int(input('Digite o valor do deposito: R$'))
                if deposito <= 0:
                    print('Valor inválido!')
                else:
                    banco.limpar()
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
                    banco.limpar()
                # END if

            elif opcao == 'q':
                print('Saindo...')
                sys.exit(2)
            else:
                print('Opção inválida!')
# END main


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
