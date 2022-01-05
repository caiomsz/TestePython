print('Progressao aritimetica v.2.0_usando while')
print('===============')
print('Gerador de PA')
print('===============')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end=' ')
    termo += razao
    cont += 1
    ##ALTERAÇÃO
