print('-='*30)
print(f'{' '*20}BOLETIM ESCOLAR')
print('-='*30)

boletim = []
materia = []
notas_temp = []
total = 0
cont = nota = 1
opc = 'S'

while opc == 'S':
    materia.append(str(input(f'{cont}° Matéria: '))) # Pega as matérias do usuário 
    print('-'*35)

    for c in range(1, 5):
        nota = (int(input(f'Digite sua nota do {c}° Bimestre: '))) # Pega as notas dos bimestres

        total += nota # Total da matéria
        
        if nota > 25 or nota < 0:
            while nota > 25 or nota < 0:
                nota = (int(input('ERRO! Nota máxima permitida é 25 por Bimestre, Tente novamente: ')))
                
        notas_temp.append(nota)
    
    print('-'*35)    
    opc = str(input('Possui mais matérias? ')).upper()[0]
    cont += 1
    print('-'*35)
    notas_temp.append(total)
    materia.append(notas_temp[:])
    boletim.append(materia[:])
    
    materia.clear()
    notas_temp.clear()
    total = 0

#for materia in boletim[][0]:
 #   for nota,enumerate in boletim[][1]
    