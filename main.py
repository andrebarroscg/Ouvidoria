"""

Andre Tadeu Vasconcelos Lins de Barros

"""
from ouvidoria import *

opcao = "Abella's Systems"
conexao = abrirBancoDados('localhost','root','88103432','ouvidoria')

while opcao != '5':
    opcao = menu()

    if opcao == '1':
        listarReclamacoes(conexao)

    elif opcao == '2':
        inserirReclamacoes(conexao)

    elif opcao == '3':
        removerReclamacoes(conexao)

    elif opcao == '4':
        pesquisarReclamacoes(conexao)

    elif opcao == '5':
        agradecimento()

    elif opcao != '5':
        opcaoInvalida()

encerrarBancoDados(conexao)


