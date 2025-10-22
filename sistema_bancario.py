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
        self.agencia = '0001'
        self.menu = 1
        self.usuarios = []
        self.contas = []
        self.numero_contas = len(self.contas)
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
    [c]\t Criar Conta
    [q]\t Sair

    Ou entrar com CPF => """
    return input(textwrap.dedent(menu))


# Criar Usuário
def criar_usuario(usuarios):
    limpar()
    print('===== Novo Usuário =====')
    print('Bem vindo ao Banco Heisu.')
    
    cpf = input('Digite seu CPF => ')
    if cpf.isnumeric():
        # Confere se usuário já é cadastrado
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print(f'Usuário {usuario} já existente')
            return

        nome = input('Informe seu nome completo: ')
        limpar()
        # data_nascimento = input('Informe sua data de nascimento (dd--mm--aaaa): ')
        limpar()
        print('Informe seu endereço:')
        endereco = input('- Logradouro: ')
        endereco += ', '
        endereco += input('- No:')
        endereco += ' - '
        endereco += input('- Bairro: ')
        endereco += ', '
        endereco += input('- Cidade: ')
        endereco += '/'
        endereco += input('- Sigla Estado: ')

        limpar()
        print(f'Bem vindo(a) {nome}.')
        user = False

        while user is False:
            senha = input('Digite sua senha => ')
            if senha.isnumeric():
                usuario = {str(cpf): senha}
                user = True
                print('Senha criada com sucesso!')
            else:
                print('Use apenas números inteiros.\nTente novamente. ')
                timer(2)
                continue
            # END if
        # END while
        
        return {'nome': nome, 'cpf': int(cpf), 'endereco': endereco, 'senha': senha}


# Filtrar Usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == int(cpf)]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

# Criar Conta
def criar_conta(agencia, numero_conta, usuarios):
    limpar()
    numero_conta += 1
    usuario = False
    while usuario is False:
        try:
            cpf = int(input('Digite seu CPF => '))
            # Confere se usuário já é cadastrado
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                print(f'Olá {usuario['nome']}, \nsua conta {numero_conta} foi criada com sucesso na agencia {agencia}')
                user = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
                timer()
            else:
                print(f'Usuário {cpf} - {type(cpf)} - Não encontrado.')
                user = None
                timer()
        except Exception:
            continue
        
    return user


# Listar Contas
def listar_contas(contas):
    limpar()
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        print(textwrap.dedent(linha))
        
    print('='*100, end='\n\n')
    input('Pressione ENTER para retornar ao menu principal. ')
    

# Autenticação
def autenticacao(usuario):
    tentativa = 1
    while tentativa <= 3:
        senha = str(input("Digite sua senha => "))
        if senha != str(usuario['senha']):
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
    [lc]\t Listar Contas
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
            input('Pressione ENTER para retornar ao menu principal. ')
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


# Exibir Extrato
def extrato(transacoes, /, *, Extrato):
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
            [c]\t Criar Conta
            [q]\t Sair
            Ou entrar com CPF =>
            """
            opcao1 = menu1()

            if opcao1 == 'u':
                # Criar Novo Usuário
                banco.usuarios.append(criar_usuario(banco.usuarios))
                timer()

            elif opcao1 == 'c':
                # Criar Nova Conta
                
                conta = criar_conta(agencia=banco.agencia, numero_conta=banco.numero_contas, usuarios=banco.usuarios)
                if conta:
                    banco.contas.append(conta)
                    banco.numero_contas += 1
                else:
                    print('Não foi possível criar uma conta.')

            elif opcao1 == 'q':
                print('Saindo', end='')
                timer()
                sys.exit(2)

            elif opcao1.isnumeric():
                limpar()
                usuario = filtrar_usuario(cpf=opcao1, usuarios=banco.usuarios)
                autorizado = autenticacao(usuario)
                autorizado = True
                print(f'Usuário {usuario['nome']} autorizado. ')
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
            limpar()
            
            opcao2 = menu2()

            # Caso número de transações diárias passar do limite estipulado
            if banco.n_transacoes_diarias == banco.LIMITE_TRANSACOES:
                print('Você atingiu seu limite diário de 10 transações.')
                print('Encerrando.')
                timer()
                sys.exit(2)
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
                    input('Pressione ENTER para retornar ao menu principal. ')
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
                        input('Pressione ENTER para retornar ao menu principal. ')
                    else:
                        print('Valor de saque nulo.')
                    # END if                    
                    
                    limpar()

                elif opcao2 == 'e':
                    extrato(banco.transacoes, Extrato=banco.Extrato)
                                     
                    input('Pressione ENTER para retornar ao menu principal. ')
                    limpar()

                elif opcao2 == 'lc':
                    listar_contas(banco.contas)

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
