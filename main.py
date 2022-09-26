import re


# Opções do Menu Principal. #
def menu_principal_info():
    print('\n\t####################################################################', end='')
    print('\n\t===================== CADASTRO DE FUNCIONÁRIOS =====================')
    print('\t####################################################################')
    print('\n\t1 - Cadastrar Funcionário\n\t2 - Pesquisar Funcionário')
    print('\t3 - Cadastrar Novo Telefone\n\t4 - Editar Dados do Funcionário')
    print('\t5 - Deletar Funcionário\n\t0 - Sair\n')
    print('\t####################################################################')
    print('\t####################################################################')


# Lista de Funcionários. #
lista_de_funcionarios = []


# Função para cadastrar um Novo Funcionario. #
def novo_funcionario(nome, cpf, cargo, salario, telefone):
    funcionario = {'nome': nome,
                   'cpf': cpf,
                   'cargo': cargo,
                   'salario': salario,
                   'telefones': [telefone]}
    return funcionario


# Função para Editar Informações de um Funcionário. #
def editar_funcionario(funcionario, nome, cpf, cargo, salario, telefone):
    funcionario['nome'] = nome
    funcionario['cpf'] = cpf
    funcionario['cargo'] = cargo
    funcionario['salario'] = salario
    funcionario['telefones'] = [telefone]


# Função para Econtrar um Funcionário. #
def buscar_funcionario(cpf):
    for funcionario in lista_de_funcionarios:
        if funcionario['cpf'] == cpf:
            return funcionario


# Função para Imprimir os Dados de um Funcionário. #
def imprimir_funcionario(funcionario):
    print('\t--------------------------------------------------------------------')
    print('\tNome: {}'.format(funcionario['nome']))
    print('\tCPF: {}'.format(funcionario['cpf']))
    print('\tCargo: {}'.format(funcionario['cargo']))
    print('\tSalário: R$ {:.2f}'.format(funcionario['salario']))
    print('\tTelefones: {}'.format(funcionario['telefones']))
    print('\t--------------------------------------------------------------------')


# Função para Valida um Valor Repassado. #
def validar_valor(valor):
    if valor.isdigit():
        return int(valor)
    else:
        return None


# Checa se uma String pode ser Convertida para Float. #
def is_float(valor):
    if isinstance(valor, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', valor): return True
    return False


# Checa se uma String pode ser Convertida para Int. #
def is_int(valor):
    if isinstance(valor, int): return True
    if re.search(r'^\-{,1}[0-9]+$', valor): return True
    return False


# Checa se uma String pode ser Convertida para Number. #
def is_number(valor):
    return is_int(valor) or is_float(valor)


# Função que Verifica se o Valor da Entrada pode ser Convertido para Float. #
def validar_input(info):
    valor = ''
    while not is_number(valor):
        valor = input(info)
        if not is_number(valor):
            print('\n\tInforme um Valor Valido!\n')
    else:
        return float(valor)


# Função que ler e Verifica se o Valor do Salário Não é negativo. #
def ler_valor_salario():
    valor = -1
    while valor < 0:
        valor = validar_input('\tInforme o Salário: ')
        if valor < 0:
            print('\n\tInforme um Valor Maior ou Igual a R$ 0.00 para o Salario!\n')
    else:
        return valor


# Menu principal. #
def menu():
    op = None
    while op != 0:
        menu_principal_info()
        op = validar_valor(input('\n\tDigite a Opção: '))

        if op == 0:
            print('\n\tSAINDO...')
        elif op == 1:

            nome = input('\n\tInforme o Nome: ')
            cpf = input('\tInforme o CPF: ')
            cargo = input('\tInforme o Cargo: ')
            salario = ler_valor_salario()
            telefone = input('\tInforme o Telefone: ')

            lista_de_funcionarios.append(novo_funcionario(nome, cpf, cargo, salario, telefone))
            print('\n\tFuncionário Cadastrado com Sucesso!')

        elif op == 2:

            if lista_de_funcionarios:
                cpf = input('\n\tInforme o CPF do Funcionario a Buscar: ')

                funcionario = buscar_funcionario(cpf)

                if funcionario is not None:

                    print()
                    imprimir_funcionario(funcionario)

                else:
                    print('\n\tFuncionário Não Encontrada!')
            else:
                print('\n\tNão há Funcionários Cadastrados!')

        elif op == 3:

            if lista_de_funcionarios:
                cpf = input('\n\tInforme o CPF do Funcionario a Adicionar Telefone: ')

                funcionario = buscar_funcionario(cpf)

                if funcionario is not None:

                    print('\n\tFuncionário Encontrado {}.'.format(funcionario['nome']))

                    telefone = input('\n\tAdicione um Novo Telefone: ')

                    funcionario['telefones'].append(telefone)

                    print('\n\tTelefone Adicionado com Sucesso!')

                else:
                    print('\n\tFuncionário Não Encontrada!')
            else:
                print('\n\tNão há Funcionários Cadastrados!')

        elif op == 4:

            if lista_de_funcionarios:
                cpf = input('\n\tInforme o CPF do Funcionario a Editar: ')

                funcionario = buscar_funcionario(cpf)

                if funcionario is not None:

                    print('\n\tFuncionário Encontrado {}.'.format(funcionario['nome']))
                    print('\n\tEDITE AS INFORMAÇÕES DO FUNCIONÁRIO:')

                    nome = input('\n\tInforme o Nome: ')
                    cpf = input('\tInforme o CPF: ')
                    cargo = input('\tInforme o Cargo: ')
                    salario = ler_valor_salario()
                    telefone = input('\tInforme o Telefone: ')

                    editar_funcionario(funcionario, nome, cpf, cargo, salario, telefone)

                    print('\n\tDados do Funcionário Atualizados com Sucesso!')

                else:
                    print('\n\tFuncionário Não Encontrada!')
            else:
                print('\n\tNão há Funcionários Cadastrados!')

        elif op == 5:

            if lista_de_funcionarios:
                cpf = input('\n\tInforme o CPF do Funcionario a Deletar: ')

                funcionario = buscar_funcionario(cpf)

                if funcionario is not None:

                    print('\n\tFuncionário Deletado {}.'.format(funcionario['nome']))

                    lista_de_funcionarios.remove(funcionario)

                else:
                    print('\n\tFuncionário Não Encontrada!')
            else:
                print('\n\tNão há Funcionários Cadastrados!')

        else:
            print('\n\tOpção Invalida!')


menu()
