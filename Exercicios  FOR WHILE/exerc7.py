estoque  = 5
for produtos in range(5):
    produtos += 1
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque}')
print('Estoque esgotado')