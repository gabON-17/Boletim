print('-='*30)
print('BOLETIM ESCOLAR')
print('-='*30)

cont = nota = 1
matriz = []
opc = 'S'
materia = []
notas_temp = []

while opc == 'S':
    materia.append(str(input(f'{cont}° Matéria: '))) # Pega as matérias do usuário 

    for c in range(1, 5):
        nota = (int(input(f'Digite sua nota do {c}° Bimestre: '))) # Pega as notas dos bimestres
        
        if nota > 25:
            while nota > 25:
                nota = (int(input('ERRO! Nota máxima permitida é 25 por Bimestre, Tente novamente: ')))
        
        notas_temp.append(nota)
        
    opc = str(input('Possui mais matérias? ')).upper()[0]
    cont += 1

    materia.append(notas_temp[:])
    matriz.append(materia[:])
    
    materia.clear()
    notas_temp.clear()
print(matriz)