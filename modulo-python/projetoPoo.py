class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.status_de_emprestimo = True

class Membro:
    def __init__(self, id_membro: int, nome: str):
        self.id_membro = id_membro
        self.nome = nome
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []
        self.proximo_id_livro = 1
        self.proximo_id_membro = 1
        
    def adicionar_livro(self):
        titulo = input("Digite o título do livro que deseja adicionar: ")
        autor = input("Digite o autor do livro: ")
        novo_livro = Livro(self.proximo_id_livro, titulo, autor)
        self.catalogo_livros.append(novo_livro)
        self.proximo_id_livro += 1
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def adicionar_membro(self):
        nome = input("Digite o nome do membro para cadastro: ")
        novo_membro = Membro(self.proximo_id_membro, nome)
        self.registro_membros.append(novo_membro)
        self.proximo_id_membro += 1
        print(f"Membro '{nome}' cadastrado com sucesso!")

    def buscar_livro(self):
        consulta = input("Digite o título, autor ou ID do livro: ").lower()
        resultados = []
        for livro in self.catalogo_livros:
            if consulta in livro.titulo.lower() or consulta in livro.autor.lower() or consulta == str(livro.id_livro):
                resultados.append(livro)
        if resultados:
            for livro in resultados:
                status = "Disponível" if livro.status_de_emprestimo else "Emprestado"
                print(f"""
                      ID: {livro.id_livro}
                      Título: {livro.titulo}
                      Autor: {livro.autor}
                      Status: {status}
""")
        else:
            print("Nenhum livro encontrado.")

    def mostrar_todos_livros(self):
        if self.catalogo_livros:
            for livro in self.catalogo_livros:
                status = "Disponível" if livro.status_de_emprestimo else "Emprestado"
                print(f"""
                      ID: {livro.id_livro}
                      Título: {livro.titulo}
                      Autor: {livro.autor}
                      Status: {status}
""")
        else:
            print("Nenhum livro cadastrado.")

    def mostrar_todos_membros(self):
        if self.registro_membros:
            for membro in self.registro_membros:
                print(f"""
                      ID: {membro.id_membro}
                      Nome: {membro.nome}
""")
        else:
            print("Nenhum membro cadastrado.")

    def emprestar_livro(self):
        self.mostrar_todos_livros()
        livro_id = int(input("Digite o ID do livro que deseja emprestar: "))
        for livro in self.catalogo_livros:
            match livro:
                case Livro(id_livro=livro_id, status_de_emprestimo=True):
                    self.mostrar_todos_membros()
                    membro_id = int(input("Digite o ID do membro que irá pegar emprestado: "))
                    for membro in self.registro_membros:
                        match membro:
                            case Membro(id_membro= membro_id):
                                livro.status_de_emprestimo = False
                                membro.historico.append(livro)
                                print(f"Livro '{livro.titulo}' emprestado para '{membro.nome}'.")
                                return
                    print("Membro não encontrado.")
                    return
                case Livro(id_livro=livro_id, status_de_emprestimo=False):
                    print("Livro já emprestado.")
                    return
        print("Livro não encontrado.")

    def devolver_livro(self):
        self.mostrar_todos_livros()
        livro_id = int(input("Digite o ID do livro que deseja devolver: "))
        for livro in self.catalogo_livros:
            if livro.id_livro == livro_id:
                match livro:
                    case Livro(id_livro=livro_id, status_de_emprestimo=False):
                        livro.status_de_emprestimo = True
                        print(f"Livro '{livro.titulo}' devolvido com sucesso!")
                        return
                    case Livro(id_livro=livro_id, status_de_emprestimo=True):
                        print("Livro não está emprestado.")
                        return
        print("Livro não encontrado.")

def main():
    biblioteca = Biblioteca()
    while True:
        print("1. Adicionar Livro")
        print("2. Adicionar Membro")
        print("3. Buscar Livro")
        print("4. Mostrar Todos os Livros")
        print("5. Mostrar Todos os Membros")
        print("6. Emprestar Livro")
        print("7. Devolver Livro")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                biblioteca.adicionar_livro()
            case "2":
                biblioteca.adicionar_membro()
            case "3":
                biblioteca.buscar_livro()
            case "4":
                biblioteca.mostrar_todos_livros()
            case "5":
                biblioteca.mostrar_todos_membros()
            case "6":
                biblioteca.emprestar_livro()
            case "7":
                biblioteca.devolver_livro()
            case "8":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()