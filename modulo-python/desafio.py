control_vendas = []

import random
from random import choice

while True:
    nome_cliente = str(input("Digite o nome do cliente ou 'sair': ")).strip()
    if nome_cliente.lower() == 'sair':
        break
    else:
        valor_compra = float(input("Digite o preço da compra: "))
        nome_produto = str(input("Digite o nome do produto: "))
        quantidade_produtos = int(input('Digite a quantidade de produtos comprados: '))

        controle = {
            'nome':nome_cliente,
            'preço': valor_compra,
            'quantidade': quantidade_produtos
        }

        control_vendas.append(controle['nome'])

    
print ('O vencedor do sorteio e o produto comprado foi: ')
print (choice(control_vendas))

maior_valor = controle['preço']

for vendas_da_vez in control_vendas:
    if vendas_da_vez['preço'] > maior_valor:
        maior_valor = vendas_da_vez['preço']
        # cliente1 = vendas_da_vez['nome']

    


print(f'A compra mais cara foi R${maior_valor} reais feita por ')

# menor_valor = controle["Preço"]

# for vendas_da_vez in control_vendas:
#     if vendas_da_vez["Preço"] < menor_valor:
#        menor_valor = vendas_da_vez["Preço"]
#        clienteb = vendas_da_vez["Nome"]
    

# print(f'A compra mais barata foi R${menor_valor} reais feita por {clienteb}')