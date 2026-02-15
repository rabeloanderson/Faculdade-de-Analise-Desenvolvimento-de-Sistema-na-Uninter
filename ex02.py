preco = float(input('Digite o preço do produto: R$ ').replace(',', '.'))
desconto = float(input('Digite o percentual de desconto: ').replace(',', '.'))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Preço final do produto: R$ {preco_final:.2f}')
