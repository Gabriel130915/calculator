import _tkinter
from multiprocessing.sharedctypes import Value
from time import sleep


#calculadora
def ponto():
    print('-'*11)
    

ponto()
print('CALCULADORA')
ponto()

numero1 = None
numero2 = None
escolha = None
opcao_invalida = False

# 0 Melhoria - Orientar a obj
# 1 Melhoria - Implentar o Loop Eterno
# 2 Melhoria - Entradas de usuário
# 3 Melhoria - Nomeação das variaveis
# 4 Melhoria - Implementar Menu (e Tratamento de Exceção)

while True:
    """
    operacoes_validas = {
        1: ['ADIÇÃO', '+', lambda x, y: x + y],
        2: ['SUBTRAÇÃO', '-', lambda x, y: x - y],
    }
    
    [1] - ADIÇÃO
    [2] - SUBTRAÇÃO
    [3] - MULTIPLICAÇÃO
    [4] - DIVISÃO
    [5] - POTENCIAÇÃO
    [ ]
    [999] - SAIR
    
    
    """
    
    if not numero1: 
        numero1 = int(input("Digite o primeiro número: ") or 0)
    print()

    if not numero2:
        numero2 = int(input("Digite o segundo número: ") or 0)
    print()
    
    if not escolha or opcao_invalida:
        escolha = input('Digite a operação desejada [+ - * /]: ')

    if escolha == '+':
        resultado = (numero1 + numero2) 
        print('O soma de {} + {} é {}'.format(numero1, numero2, resultado ))
        print()
        sleep(1)  
    elif escolha == '-':
        resultado = (numero1 - numero2) 
        print('A subtração de {} - {} é {}'.format(numero1, numero2, resultado))
        print()
        sleep(1) 
    elif escolha == '*' or escolha == 'x':
        resultado = (numero1 * numero2)
        print('A multiplicação de {} x {} é {}'.format(numero1, numero2, resultado))
        print()
        sleep(1) 
    elif escolha == '/':
        resultado = (numero1 / numero2)
        print('A divisão entre {} e {} é {}'.format(numero1, numero2, resultado))
        print()
        sleep(1)   
    else:
        print('Operação inválida! Operações suportadas: +, -, *, /')
        opcao_invalida = True
        continue

    opcao = input('Deseja continuar? [S/N]: ').upper()

    if opcao == 'N':
        print()
        print('Carregando...')
        sleep(1)
        print('PROGRAMA ENCERRADO!')
        break 
    
    else:
        numero1 = None
        numero2 = None
        escolha = None
        opcao_invalida = False
    
    
