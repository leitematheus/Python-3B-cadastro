clientes = []

def cadastro_clientes():
    print('Cadastrar Clientes')
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do Cliente: ')
    # Aqui você pode adicionar o código para cadastro de clientes
    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone
    }

    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def listar_clientes():
    print('Listar Clientes')
    # Aqui você pode adicionar o código para listar clientes

def ativar_cliente():
    print('Ativar/Desativar Cliente')
    # Aqui você pode adicionar o código para ativar ou desativar clientes

def sair_aplicacao():
    print('Saindo da Aplicação')
    # Aqui você pode adicionar o código para encerrar a aplicação

def exibir_menu():
    print('''
      
          Gelados Gourmet
          
          1. Cadastro de Clientes
          2. Listar Clientes
          3. Ativar Cliente
          4. Sair da aplicação
          
      ''')

while True:
    exibir_menu()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastro_clientes()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            ativar_cliente()
        elif opcao_escolhida == 4:
            sair_aplicacao()
            break  # Saí do loop para encerrar o programa
        else:
            print('Opção inválida! Por favor, escolha uma opção entre 1 e 4.')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número.')
        