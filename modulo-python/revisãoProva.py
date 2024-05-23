def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))

    total = quantidade * valor_unitario
    produto = {"nome": nome, "valor": valor_unitario, "quantidade": quantidade, "total": total}
    lista_produtos.append(produto)

    print("Produto adicionado com sucesso!\n")


def ver_lista(lista_produtos):
    if not lista_produtos:
        print("A lista de produtos está vazia.")
    else:
        print("Lista de produtos:")
        for produto in lista_produtos:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor unitário: R${produto['valor']}, Total: R${produto['total']}")
        print(f"Valor total de todos os produtos: R${sum(produto['total'] for produto in lista_produtos)}\n")


def atualizar_produto(lista_produtos):
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_produtos:
        if produto["nome"] == nome:
            quantidade = int(input("Digite a nova quantidade do produto: "))
            valor_unitario = float(input("Digite o novo valor unitário do produto: "))

            produto["quantidade"] = quantidade
            produto["valor"] = valor_unitario
            produto["total"] = quantidade * valor_unitario

            print("Produto atualizado com sucesso!\n")
            return
    print("Produto não encontrado.\n")


def remover_produto(lista_produtos):
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_produtos:
        if produto["nome"] == nome:
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!\n")
            return
    print("Produto não encontrado.\n")


def menu():
    lista_produtos = []
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_produto(lista_produtos)
        elif opcao == "2":
            ver_lista(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos)
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
