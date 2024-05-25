class Material:
    def __init__(self, titulo:str, autor_ou_editora: str) -> None:
        self.titulo=titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        return f' Título do livro: {self.titulo} e autor ou editora: {self.autor_ou_editora}'
    

class Livro(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, genero: str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    def exibir_informacoes(self):
        return f' Genero do livro: {self.genero}'
    
class Revista(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, edicao: str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    def exibir_informacoes(self):
        return f'Edição da revista: {self.edicao}'
    

livro = Livro('Harry Potter e a pedra filósofal', 'J.K Rowling,', 'Fantasia')
revista = Revista('National Geographic', 'Editora Abril', 'Janeiro 2024')


print(livro.exibir_informacoes())
print(revista.exibir_informacoes())
