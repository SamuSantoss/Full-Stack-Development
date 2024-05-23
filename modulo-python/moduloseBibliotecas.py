alunos = {}  


def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")


def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")


def VerAlunos():
    if not alunos:
        print("Não há alunos cadastrados.")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
