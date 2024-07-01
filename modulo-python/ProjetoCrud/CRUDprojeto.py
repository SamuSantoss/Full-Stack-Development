import mysql.connector

configuracoes = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql102030",
    "database": "loja"
}


def atualizar(comando):
    conexao  = mysql.connector.connect(**configuracoes)
    janelinha = conexao.cursor()
    janelinha.execute(comando)
    conexao.commit()
    janelinha.close()
    conexao.close()
    return ("Banco atualizado com sucesso")

def visualizar(comando):
    conexao  = mysql.connector.connect(**configuracoes)
    janelinha = conexao.cursor()
    janelinha.execute(comando)
    todos_dos_dados = janelinha.fetchall()
    janelinha.close()
    conexao.close()
    return todos_dos_dados

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Cadastrar novo produto
    2 - Ver todos os produtos
    3 - Editar um produto
    4 - Excluir um produto
    5 - Cadastrar venda
    6 - Ver todas as vendas
    7 - Editar uma venda
    8 - Excluir uma venda
    0 - Sair
"""))
    match menu:
        case 1:
            nome = str(input("Digite o nome do produto: "))
            descricao = str(input("Digite a drecicao do produto: "))
            qntd_disponivel = int(input("Digite a quantidade disponivel do produto: "))
            preco = float(input("Digite o preco do produto: "))
            print(atualizar(f"""
                INSERT INTO produto (nome, descricao, qntd_disponivel, preco) VALUES
                ('{nome}', '{descricao}', {qntd_disponivel}, {preco});
            """))
        case 2:
            todos_produtos = visualizar("select* from produto")
            for produto in todos_produtos:
                print(f"""
                ID: {produto[0]}
                Nome: {produto[1]}
                Descricao: {produto[2]}
                Quantidade disponivel: {produto[3]}
                Preco: {produto[4]} 
                """)
        case 3:
            todos_produtos = visualizar("select* from produto")
            for produto in todos_produtos:
                print(f"""
                ID: {produto[0]}
                Nome: {produto[1]}
                Descricao: {produto[2]}
                Quantidade disponivel: {produto[3]}
                Preco: {produto[4]} 
                """)
            id_editado = int(input("Digite o id do produto que deseja editar: "))
            produto_selecionado = visualizar(f"SELECT * FROM produto WHERE id = {id_editado};")

            if not produto_selecionado:
                print("Produto não encontrado!")
                continue
            while True:
                menu = int(input(
                    """Escolha uma opção:
                    1 - alterar descrição
                    2 - alterar quantidade disponível
                    3 - alterar preço
                    4 - voltar ao menu principal
                    """
                ))
                match menu:
                    case 1:
                        descricao = str(input("Digite a nova descrição: "))
                        print(atualizar(f"""
                        UPDATE produto SET descricao = "{descricao}" WHERE id = {id_editado};
                    """))
                    case 2:
                        qntd_disponivel = int(input("Digite a nova quantidade disponivel: "))
                        print(atualizar(f"""
                        UPDATE produto SET qntd_disponivel = "{qntd_disponivel}" WHERE id = {id_editado};
                    """))
                    case 3:
                        preco = float(input("Digite o novo preço: "))
                        print(atualizar(f"""
                        UPDATE produto SET preco = "{preco}" WHERE id = {id_editado};
                    """))
                break

        case 4:
            todos_os_produtos =  visualizar("SELECT * FROM produto")
            produtos_disponiveis = []
            for produto in todos_os_produtos:
                produtos_disponiveis.append(produto[0])
                print(f"""
                ID: {produto[0]}
                Título: {produto[1]}
            """)
                
            id_excluido = int(input("Digite o ID do produto que você deseja deletar: "))
            produto= visualizar(f"SELECT * FROM produto WHERE id = {id_excluido};")

            if not produto:
                print("Produto não encontrado!")
                continue

            confirmacao = input("Tem certeza que deseja excluir este produto? (S/N): ").upper()

            match confirmacao:
                case "S":
                    print(atualizar(f"DELETE FROM produto WHERE id = {id_excluido};"))
                    print("Produto excluído com sucesso!")
                case "N":
                    print("Operação de exclusão cancelada.")
                case _:
                    print("Opção inválida!")
        case 5:
            todos_produtos = visualizar("SELECT * FROM produto")
            produtos_disponiveis = []
            for produto in todos_produtos:
                produtos_disponiveis.append(produto[0])
                print(f"""
                ID: {produto[0]}
                Nome: {produto[1]}
                Quantidade disponível: {produto[3]}
                """)

            id_produto = int(input("Digite o ID do produto que você deseja vender: "))
            if id_produto in produtos_disponiveis:
                qntd_vendida = int(input("Digite a quantidade vendida: "))
                data_venda = str(input("Digite a data da venda (YYYY-MM-DD): "))
                qntd_disponivel = visualizar(f"SELECT qntd_disponivel FROM produto WHERE id = {id_produto};")[0][0]
                qntd_atualizada = qntd_disponivel - qntd_vendida
                if qntd_vendida > qntd_disponivel:
                    print("Quantidade indisponível no estoque!")
                else:
                    print(atualizar(f"""
                    insert into venda (id_produto, qntd_vendida, data_venda) values
                        ({id_produto}, {qntd_vendida}, "{data_venda}");
                    """))
        
                    print(atualizar(f"""
                        UPDATE produto SET qntd_disponivel = "{qntd_atualizada}" WHERE id = {id_produto};
                    """))
                 
            else: 
                print("Produto não encontrado. Não é possivel realizar a venda!")
            
        case 6:
            todas_vendas = visualizar("""
                SELECT venda.id, produto.nome, venda.qntd_vendida, venda.data_venda  FROM venda
                JOIN produto ON venda.id_produto = produto.id
            """)
                 
            for venda in todas_vendas:
                print(f"""
                ID da Venda: {venda[0]}
                Nome do Produto: {venda[1]}
                Quantidade Vendida: {venda[2]}
                Data da Venda: {venda[3]}
            """)
        case 7:
            todas_vendas = visualizar("""
                SELECT venda.id, produto.nome, venda.qntd_vendida, venda.data_venda
                FROM venda
                JOIN produto ON venda.id_produto = produto.id
            """)
            for venda in todas_vendas:
                print(f"""
                ID da Venda: {venda[0]}
                Nome do Produto: {venda[1]}
                Quantidade Vendida: {venda[2]}
                Data da Venda: {venda[3]}
                """)

            id_venda = int(input("Digite o ID da venda que deseja editar: "))
            venda_selecionada = visualizar(f"SELECT * FROM venda WHERE id = {id_venda};")

            if not venda_selecionada:
                print("Venda não encontrada!")
                continue

            while True:
                submenu = int(input("""
            Escolha o que deseja editar:
            1 - Alterar quantidade vendida
            2 - Alterar data da venda
            0 - Voltar ao menu principal
            """))

                match submenu:
                    case 1:
                        nova_qntd_vendida = float(input("Digite a nova quantidade vendida: "))
                        print(atualizar(f"""
                            UPDATE venda SET qntd_vendida = {nova_qntd_vendida} WHERE id = {id_venda};
                        """))
                    case 2:
                        nova_data_venda = input("Digite a nova data da venda (YYYY-MM-DD): ")
                        print(atualizar(f"""
                            UPDATE venda SET data_venda = '{nova_data_venda}' WHERE id = {id_venda};
                        """))
                    case 0:
                        break
                    case _:
                        print("Opção inválida!")
        case 8:
            todas_vendas = visualizar("""
                SELECT venda.id, produto.nome, venda.qntd_vendida, venda.data_venda
                FROM venda
                JOIN produto ON venda.id_produto = produto.id
            """)
            for venda in todas_vendas:
                print(f"""
                ID da Venda: {venda[0]}
                Nome do Produto: {venda[1]}
                Quantidade Vendida: {venda[2]}
                Data da Venda: {venda[3]}
                """)

            id_venda = int(input("Digite o ID da venda que deseja excluir: "))
            venda_selecionada = visualizar(f"SELECT * FROM venda WHERE id = {id_venda};")

            if not venda_selecionada:
                print("Venda não encontrada!")
                continue

            confirmacao = input("Tem certeza que deseja excluir esta venda? (S/N): ").upper()

            match confirmacao:
                case "S":
                    print(atualizar(f"DELETE FROM venda WHERE id = {id_venda};"))
                    print("Venda excluída com sucesso!")
                case "N":
                    print("Operação de exclusão cancelada.")
                case _:
                    print("Opção inválida!")

        case 0:
            print('Fim do programa')
            break
        case    _:
            print('Opção inválida')