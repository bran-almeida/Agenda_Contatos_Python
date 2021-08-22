import functions
from time import sleep

functions.import_csv('database.csv')
while True:
    functions.menu()

    escolha = str(input('>>>'))
    
    #ADICIONAR CONTATO|EDITAR CONTATO
    if escolha == '1' or escolha == '2':
        nome = str(input('NOME:\n>>> ').upper())

        if nome in functions.contatos: #Confere se o nome está presente na agenda
            print(f'O contato {nome} já existe. DESEJA EDITA-LO?')
            while True:
                sim_não = str(input('SIM[S]|NÃO[N]\n>>> ').upper())
                if sim_não == 'S':
                    print(f'EDITANDO CONTATO {nome}')
                    functions.contatos.pop(nome)
                    nome = str(input('NOME:\n>>> ').upper())
                    telefone,email,endereco = functions.read_data()
                    functions.add_edit_contato(nome,telefone,email,endereco)
                    break
                elif sim_não == 'N':
                    break
                else:
                    print('VALOR INVÁLIDO, INFORME "S" OU "N"!!!')
        else:
            print('Adicionando contato.')
            telefone,email,endereco = functions.read_data()
            functions.add_edit_contato(nome, telefone, email, endereco)
    
    #MOSTRAR CONTATOS
    elif escolha == '3':
        functions.mostrar_contatos()
    
    #BUSCAR CONTATO
    elif escolha == '4':
        busca = str(input('NOME:\n>>> ').upper())
        functions.buscar_contato(busca)
    
    #EXCLUIR CONTATO
    elif escolha == '5':
        functions.excluir_contato()
    
    #EXPORTAR CONTATOS EM .CSV
    elif escolha == '6':
        filename = str(input('Qual o nome do arquivo a ser exportado?\n>>>'))
        functions.exportar_csv(filename)

    #IMPORTAR CONTATOS .CSV
    elif escolha == '7':
        functions.import_csv(str(input('Infome o nome do arquivo a ser importado: ')))

    #SAIR
    elif escolha in ('sS'):
        print('_'*50)
        print(f'{functions.colors["red"]}Saindo{functions.colors["reset"]}')
        print('_'*50)
        break
    
    #VALOR INVALIDO
    else:
        print('_'*50)
        print(f'{functions.colors["red"]}O VALOR INFORMADO É INVALIDO, INFORME UM VALOR DE 1 A 6!!!{functions.colors["reset"]}')
        print('_'*50)
        sleep(1)