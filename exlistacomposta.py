from time import sleep
print(20 * '=')
print('Cadastros de Membros')
print(20 * '=')
membros = list()
while True:
    nome = str(input('Nome comleto:')).upper().strip()
    idade = int(input('Idade:'))
    admissao = str(input('Data de admissão:'))
    funcao = str(input('Função:[Ex: membro, diácno, pastor...]')).upper().strip()
    membros.append([nome, idade, admissao, funcao])
    resp = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if resp not in 'Ss':
        break
print(100 * '=')
print(f'{"Nu.":<8}{"Nome":<30}{"Idade":<15} {"Data Admissão":<15} {"Função":>13}')
print(100 * '=')
for i, m in enumerate(membros):
    print(f'{i:<8} {m[0]:<30} {m[1]:<15} {m[2]:<15}{m[3]:>13}')
print(100 * '=')
sleep(1)
while True:
    opc = int(input('Digite o numero do membro (a) para exibir o cadastro - [999] para sair:'))
    if opc == 999:
        print('Encerrando...')
        sleep(1)
        break
    if opc <= len(membros) -1:
        print(f' {membros[opc][0]}  idade - {membros[opc][1]} - Função - {membros[opc][3]} ')
    if opc > len(membros):
        print('nao cadastrado')

