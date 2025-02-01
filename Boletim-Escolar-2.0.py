from func import mysql, dados, interface
#  Ler as matérias do usuário e mostrar o boletim do aluno
tot_notas = 0
notas = list()

interface.titulo('meu boletim')
while True:
    materia = str(input('Matéria: '))
    
    interface.subTitulo('Digite sua notas')
    for c in range(0, 4):
        nota = dados.valida_nota(f'{c+1} Bimestre em {materia}: ')
        notas.append(nota)
        tot_notas += nota

        if c == 3:
            notas.append(tot_notas)
    interface.linha(15)
    print(notas)
    
    # mysql.com_sql(f'''insert into materias (nome) values ("{materia}"''')
