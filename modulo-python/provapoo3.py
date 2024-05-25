class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro: float, quantidade_combustivel:float) -> None:
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        total = valor/self.valor_litro
        self.quantidade_combustivel-=total
        return f'Você abasteceu {total} litros'
        
        
    def abastecer_por_litro(self, litros):
        total = litros * self.valor_litro
        self.quantidade_combustivel-=litros
        return f'Você abasteceu {litros} L, e vai pagar R$:{total} reais'

        
    def alterar_valor(self,valor):
        self.valor_litro = valor
        return f'O novo valor do combustível é R$:{self.valor_litro}'

    def alterar_combustivel(self, tipo):
        self.tipo_combustivel = tipo
        return f'O tipo de combustivel mudou para {self.tipo_combustivel}'

    def alterar_quantidade(self, quantidade):
        self.quantidade_combustivel = quantidade
        return f'A quantidade de combustível atual é {self.quantidade_combustivel} Litros'

bomba= BombaCombustivel('gasolina', 5.6, 10.000)


print(bomba.abastecer_por_valor(70))
print(bomba.abastecer_por_litro(15))
print(bomba.alterar_valor(4.90))
print(bomba.alterar_combustivel('alcool'))
print(bomba.alterar_quantidade(12000))
