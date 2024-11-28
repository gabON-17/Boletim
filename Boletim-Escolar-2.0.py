print('-='*30)
print(f'{' '*20}BOLETIM ESCOLAR')
print('-='*30)

boletim = []
temp = []
total = 0
cont = nota = 1
opc = 'S'

while opc == 'S':
    temp.append(str(input(f'{cont}° Matéria: ')).upper()) # Pega as matérias do usuário 
    print('-'*35)

    for c in range(1, 5):
        nota = (int(input(f'Digite sua nota do {c}° Bimestre: '))) # Pega as notas dos bimestres

        total += nota # Total da matéria
        
        if nota > 25 or nota < 0:
            while nota > 25 or nota < 0:
                nota = (int(input('ERRO! Nota máxima permitida é 25 por Bimestre, Tente novamente: ')))
                
        temp.append(nota)
    
    print('-'*35)    
    opc = str(input('Possui mais matérias? ')).upper()[0]
    cont += 1
    print('-'*35)
    
    temp.append(total)
    boletim.append(temp[:])
    
    temp.clear()
    total = 0

for list in boletim:
    print(f''' {list[0]:-^20}

    1° BIMESTRE: {list[1]}
    2° BIMESTRE: {list[2]}
    3° BIMESTRE: {list[3]}
    4° BIMESTRE: {list[4]}

    TOTAL = {list[5]}
''')
    print('Você Passou!'if list[5] >= 60 else 'Você não Passou...')
    print()
print('FIM')