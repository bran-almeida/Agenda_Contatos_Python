from time import sleep

colors = {'red':'\033[1;31m', 'green':'\033[1;32m', 'reset': '\033[0;0m'}
contatos = {}

#MENU
def menu():
    print('_'*50)
    print(f'{colors["green"]}MENU{colors["reset"]}'.center(50))
    print('[1] ADICIONAR CONTATOS')
    print('[2] EDITAR CONTATOS')
    print('[3] MOSTRAR TODOS OS CONTATOS')
    print('[4] BUSCAR CONTATO')
    print('[5] EXCLUIR CONTATOS')
    print('[6] EXPORTAR CONTATOS PARA CSV')
    print('[7] IMPORTAR CONTATOS CSV')
    print('[S] SAIR')
    print('_'*50)

#ENTRADA DE DADOS DO CONTATO
def read_data():
    telefone = str(input('TELEFONE:\n>>> '))
    email = str(input('EMAIL:\n>>>'))
    endereco = str(input('ENDEREÇO:\n>>> '))
    return telefone, email, endereco

#ADICIONAR/EDITAR CONTATO
def add_edit_contato(nome, telefone=None, email=None, endereco=None):
    """Adiciona ou edita um contato a lista de contatos"""
    try:
        nome = nome
        email = email.lower()
        endereco = endereco.upper().replace(",", ";")
        contatos[nome] = {
            'Telefone': telefone,
            'Email': email,
            'Endereço': endereco,
        }  
    except:
        print('_'*50)
        print(f'{colors["red"]}Ocorreu um erro ao salvar o contato, tente novamente.{colors["reset"]}')
        print('_'*50)
        sleep(1)   
    else:
        print('_'*50)
        print(f'{colors["green"]}Contato {nome} salvo/editado com sucesso.{colors["reset"]}')
        print('_'*50)
        exportar_csv('database')
        sleep(0.2)

#MOSTRAR CONTATOS SALVOS
def mostrar_contatos():
    """Mostra todos os contatos da lista de contatos"""
    if contatos:
        for c in contatos:
            buscar_contato(c)
    else:
        print('_'*50)
        print(f'{colors["red"]}A agenda está vazia{colors["reset"]}')
        sleep(1)
        print('_'*50)

#BUSCAR CONTATO
def buscar_contato(nome):
    if nome in contatos:
        print("_"*50)
        print(f'Nome: {nome}')
        print(f'Telefone:{contatos[nome]["Telefone"]}')
        print(f'Email: {contatos[nome]["Email"]}')
        print(f'Endereço: {contatos[nome]["Endereço"]}')
        print("_"*50)
        sleep(0.3)
    else:
        print('_'*50)
        print(f'{colors["red"]}Contato não encontrado{colors["reset"]}')
        print('_'*50)
        sleep(0.3)

#EXCLUIR CONTATO
def excluir_contato():
    nome = str(input('NOME DO CONTATO QUE DESEJA EXCLUIR:\n>>> ').upper())
    try:
        contatos.pop(nome)
        print('_'*50)
        print(f'{colors["green"]}Contato {nome} excluido com sucesso.{colors["reset"]}')
        print('_'*50)
        exportar_csv('database')
    except KeyError:
        print('_'*50)
        print(f'{colors["red"]}Contato {nome} não existe{colors["reset"]}')
        print('_'*50)
        sleep(1)
    except:
        print('_'*50)
        print(f'{colors["red"]}Um erro inesperado ocorreu{colors["reset"]}')
        print('_'*50)
        sleep(1)

#EXPORTAR CONTATOS SALVOS EM CSV
def exportar_csv(filename):
    try: 
        with open(f'{filename}.csv', 'w') as file:
            for c in contatos:
                nome = c
                tel = contatos[c]["Telefone"]
                email = contatos[c]["Email"]
                end = contatos[c]["Endereço"]
                file.write(f'{nome},{tel},{email},{end}\n')
        print('Your contacts has saved.')
    except Exception as e:
        print('Some error has occurred.')
        print(e)

#IMPORTAR CONTATOS DE UM ARQUIVO CSV
def import_csv(filename):
    try:
        with open(filename, 'r') as file:
            lines=file.readlines()
            for l in lines:
                dados_contato = l.strip().split(',')
                nome = dados_contato[0]
                telefone = dados_contato[1]
                email = dados_contato[2]
                endereco = dados_contato[3]
        
                contatos[nome] = {
                'Telefone': telefone,
                'Email': email,
                'Endereço': endereco
        }
        exportar_csv('database')  

    except FileNotFoundError:
        print('Arquivo não encontrado')