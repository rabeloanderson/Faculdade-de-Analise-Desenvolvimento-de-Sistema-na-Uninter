km = float(input('Digite a quantidade de km percorridos: ').replace(',', '.'))
dias = int(input('Digite a quantidade de dias alugados: '))

custo_dias = dias * 60
custo_km = km * 0.15
total = custo_dias + custo_km

print(f'Custo por {dias} dia(s): R$ {custo_dias:.2f}')
print(f'Custo por {km:.1f} km rodados: R$ {custo_km:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
