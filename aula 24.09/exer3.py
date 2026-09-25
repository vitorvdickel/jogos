'''
Uma loja possui um produto com estoque inicial de 10 unidades.
Crie um algoritmo que permita ao usuário controlar esse estoque por meio de um menu de opções.
Regras:
O estoque começa com 10 unidades.
O estoque não pode ultrapassar 10 unidades.
O estoque não pode ficar abaixo de 0.
Caso o usuário tente adicionar além do limite, o programa deve informar que a operação 
é inválida. 
'''

estoque = 10
opcao = ""

print ("=== CONTROLE DE ESTOQUE ===")
print ("Estoque inicial: 10 unidades")

while opcao != 4:
    print("\nEscolha uma opção: ")
    print("1 - Adicionar unidades")
    print("2 - Remover unidades")
    print("3 - Exibir estoque")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada:\n"))

    if (opcao == 1):
        adicionar = int(input("Quantas unidades você deseja adicionar ao estoque?\n"))
        estoque = estoque + adicionar
    elif (opcao == 2):
        remover = int(input("Quantas unidades você deseja remover do estoque?\n"))
        estoque = estoque - remover
    elif (opcao == 3):
        print ("Você possui", estoque, " unidades em estoque")
    else:
        print("Opção inválida")