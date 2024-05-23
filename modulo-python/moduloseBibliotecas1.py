import moduloseBibliotecas

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Atualizar aluno")
        print("4. Ver alunos")
        print("0. Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            moduloseBibliotecas.AdicionarAluno()
        elif opcao == "2":
            moduloseBibliotecas.RemoverAluno()
        elif opcao == "3":
            moduloseBibliotecas.AtualizarAluno()
        elif opcao == "4":
            moduloseBibliotecas.VerAlunos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()