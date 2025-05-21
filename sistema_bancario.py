import os
import sys
import time

class banco():
    def __init__(self):
        self.MENU = """[s] Saque\n[e] Extrato\n[d] Deposito\n[q] Sair"""
        self.USER = 'Lucas'
        self.SENHA = int(112358)
        self.saldo = 0.0
        self.limite = 500.0
        self.limite_saque = 3
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
    banco_instance = banco()

    while True:
        # Executa o método run da classe banco
        banco_instance.run()
        # Exibe o menu
        print(banco_instance.MENU)
        # Lê a opção do usuário
        opcao = input('Escolha uma opção: ')
        # Verifica a opção escolhida
        if opcao == 's':
            banco_instance.limpar()
            print('Saque')
            if banco_instance.limite_saque == 0:
                print(f'Limite de 3 saques diários atingido!')
                wait = input('Pressione ENTER para retornar ao menu principal...')
                continue
            
            print(f'Valor disponível: R${banco_instance.saldo:.2f}')
            saque = int(input('Digite o valor do saque: R$'))
            if saque > banco_instance.limite:
                print(f'Valor acima do permitido para saque! Limite máximo: R${banco_instance.limite:.2f}')
            elif saque <= 0:
                print('Valor inválido!')
            elif saque > banco_instance.saldo:
                print('Saldo insuficiente!')
            else:
                banco_instance.limpar()
                banco_instance.saldo -= saque   # Atualiza o saldo
                banco_instance.limite_saque -= 1  # Atualiza o limite de saques
                # Atualiza o extrato
                banco_instance.Extrato['Saldo do dia'] = banco_instance.saldo
                # Atualiza Transações
                saque_id = str(len(banco_instance.transacoes) + 1) + ' Saque'
                banco_instance.transacoes.update({saque_id: saque})
                print(f'Saldo atual: R${banco_instance.saldo:.2f}')
                # Exibe mensagem de sucesso
                print(f'Saque de R${saque:.2f} realizado com sucesso!')
            wait = input('Pressione ENTER para retornar ao menu principal...')

        elif opcao == 'e':
            banco_instance.limpar()
            print('Extrato')
            print('===========================')
            print(f'Saldo Anterior: R${banco_instance.Extrato["Saldo Anterior"]:>9.2f}')
            for key, value in banco_instance.transacoes.items():
                print(f'{key:<14}: R${value:>9.2f}')
            print(f'Saldo do dia  : R${banco_instance.Extrato["Saldo do dia"]:>9.2f}')
            print('===========================')
            wait = input('Pressione ENTER para retornar ao menu principal...')
        
        elif opcao == 'd':
            banco_instance.limpar()
            print('Deposito')
            print(f'Valor disponível: R${banco_instance.saldo:.2f}')
            deposito = int(input('Digite o valor do deposito: R$'))
            if deposito <= 0:
                print('Valor inválido!')
            else:
                banco_instance.limpar()
                banco_instance.saldo += deposito  # Atualiza o saldo
                # Atualiza o extrato
                banco_instance.Extrato['Saldo do dia'] = banco_instance.saldo
                # Atualiza Transações
                deposito_id = str(len(banco_instance.transacoes) + 1) + ' Deposito'
                banco_instance.transacoes.update({deposito_id: deposito})
                print(f'Saldo atual: R${banco_instance.saldo:.2f}')
                # Exibe mensagem de sucesso
                print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
                wait = input('Pressione ENTER para retornar ao menu principal...')
                banco_instance.limpar()
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
