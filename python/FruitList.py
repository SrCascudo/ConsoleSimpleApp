from time import sleep
from os import system, name as os_name

def chamar_menu():
    print('----------------------------------------------------')
    print('|         Olá! Bem vindo(a) ao FrutList!           |')
    print('----------------------------------------------------')
    print('| [1] - Adicionar uma fruta a sua lista            |')
    print('| [2] - Remover uma fruta a sua lista              |')
    print('| [3] - Visualizar a sua lista                     |')
    print('| [0] - Encerrar FrutList                          |')
    print('----------------------------------------------------')
    return input('Selecione a Opção: ')

def adicionar():
    limpar_console()
    print('----------------------------------------------------')
    print('| * Para Adicionar Informe a Fruta e Aperte Enter  |')
    print('| * Para Voltar Não Informe Valor e Aperte Enter   |')
    print('----------------------------------------------------')
    visualizar(cabecalho=False)
    
    res = input('Fruta: ')
    if len(res) != 0:
        with open('fruit_list.txt', mode='a', encoding='UTF-8') as fruit_list:
            fruit_list.write(f'{res}\n')
        adicionar()
    else:
        return
        

def remover():
    limpar_console()
    print('----------------------------------------------------')
    print('| * Para Remover Informe a Fruta e Aperte Enter    |')
    print('| * Para Voltar Não Informe Valor e Aperte Enter   |')
    print('|                                                  |')
    print('| OBS: Informe o NOME exato da fruta para excluí-la|')
    print('| caso contrário ela não será apagada              |')
    print('----------------------------------------------------')
    visualizar(cabecalho=False)

    with open('fruit_list.txt', mode='r', encoding='UTF-8') as fruit_list:
        lines = fruit_list.readlines() 
        fruta = input('Fruta: ')
        if len(fruta) != 0:
            with open('fruit_list.txt', mode='w', encoding='UTF-8') as fruit_list:
                for line in lines:
                    if line.strip('\n').lower() != fruta.lower():
                        fruit_list.write(line)
            
            remover()
        else:
            return;


def visualizar(cabecalho = True):
    if cabecalho:
        limpar_console()
        print('----------------------------------------------------')
        print('| * Para Voltar Aperte Enter                       |')
        print('----------------------------------------------------')
        print('')

    with open('fruit_list.txt', mode='r', encoding='UTF-8') as fruit_list:

        print('                      FRUTAS                        ')
        print('----------------------------------------------------')
        for line in fruit_list.readlines():
            print(f'| {adicionar_espaco(line, 50)} |')
        print('----------------------------------------------------')

    if cabecalho:
        input(':')

def encerrar():
    print('Até a próxima. Bye Bye ^-^')
    sleep(1.5)
    limpar_console()

def processar(resposta):
    reexibir_menu = True

    if resposta == '0':
        encerrar()
        reexibir_menu = False
    elif resposta == '1':
        adicionar()
    elif resposta == '2':
        remover()
    elif resposta == '3':
        visualizar()
    else:
        print('Ops! Parece que o valor que você informou não corresponde as alternativas, por favor informar um valor válido.')
        input('Pressione Enter para continuar:')

    return reexibir_menu

def limpar_console():
    if os_name == 'nt':
        system('cls')
    else:
        system('clear')

def adicionar_espaco(line, max_char):
    espacos = ''
    for i in range(1, (max_char-len(line))):
        espacos += ' '
    return line.strip('\n') + espacos

def criarArquivo():
    try:
        with open('fruit_list.txt', 'x') as arq:
            pass
    except FileExistsError:
        pass

criarArquivo()
while processar(chamar_menu()):
    limpar_console()
