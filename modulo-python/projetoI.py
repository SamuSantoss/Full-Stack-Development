import json


tarefas = {}


def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefas[nome] = {
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }

def listar_tarefas():
    for nome, dados in tarefas.items():
        status = "Concluída" if dados['concluida'] else "Pendente"
        print(f"Tarefa: {nome}\nDescrição: {dados['descricao']}\nPrioridade: {dados['prioridade']}\nCategoria: {dados['categoria']}\nStatus: {status}\n")

def marcar_como_concluida(nome):
    if nome in tarefas:
        tarefas[nome]['concluida'] = True
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def exibir_tarefas_por_prioridade(prioridade):
    for nome, dados in tarefas.items():
        if dados['prioridade'] == prioridade:
            status = "Concluída" if dados['concluida'] else "Pendente"
            print(f"Tarefa: {nome}\nDescrição: {dados['descricao']}\nCategoria: {dados['categoria']}\nStatus: {status}\n")

def exibir_tarefas_por_categoria(categoria):
    for nome, dados in tarefas.items():
        if dados['categoria'] == categoria:
            status = "Concluída" if dados['concluida'] else "Pendente"
            print(f"Tarefa: {nome}\nDescrição: {dados['descricao']}\nPrioridade: {dados['prioridade']}\nStatus: {status}\n")


def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (alta, média, baixa): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            nome = input("Nome da Tarefa a ser marcada como concluída: ")
            marcar_como_concluida(nome)
        elif escolha == '4':
            prioridade = input("Prioridade (alta, média, baixa): ")
            exibir_tarefas_por_prioridade(prioridade)
        elif escolha == '5':
            categoria = input("Categoria: ")
            exibir_tarefas_por_categoria(categoria)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
