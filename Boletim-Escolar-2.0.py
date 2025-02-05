from func import mysql, dados, interface
#  Ler as matérias do usuário e mostrar o boletim do aluno
cont_id_mat = cont = cont_bimestre = 0

notas = list()

interface.titulo('meu boletim')

aluno = dados.valida_str('Digite seu nome: ') # Pega o nome do aluno 
# mysql.com_sql(f'insert into alunos values (default, "{aluno}")') # Registra o aluno no banco

id_aluno = mysql.tabela('select id_aluno from alunos')
interface.subTitulo(f'Seu ID é {id_aluno[-1]}')

materias = mysql.tabela('select materias from materias') # Tem todas as matérias presente no banco de dados
id_mat = mysql.tabela('select id_materia from materias')


interface.subTitulo('Digite sua notas')

# for valor in materias:
        # tot_notas = 0
        # for c in range(0, 4):
            # nota = dados.valida_nota(f'{c+1} Bimestre em {valor}: ')
            # notas.append(nota)
# 
            # tot_notas += nota

            # if c == 3:
                # notas.append(tot_notas)
                # mysql.com_sql(f'insert into notas values (default, "{id_aluno[-1]}", "{id_mat[cont_id_mat]}", "{notas[0]}", "{notas[1]}", {notas[2]}, "{notas[3]}", "{notas[4]}" )')
                # cont_id_mat += 1
                # notas.clear()
# 
        # interface.linha(15)


while True:
    id = dados.validaInt('Digite seu ID: ')

    if id > id_aluno[-1]:
        print('Esse ID não existe favor digite novamente.')
        continue
    else:
        boletim = mysql.tabela(f'''select al.nome, m.materias, n.pri_Bimestre, n.seg_Bimestre, n.ter_Bimestre, n.quar_Bimestre, n.total from notas n
        join alunos al 
        on al.id_aluno = n.aluno
        join materias m
        on m.id_materia = n.materia
        where n.aluno = "{id}"''')
        break

interface.linha(30)
for item in boletim:
    cont += 1
    if cont == 1: # Para printar o nome de usuário
        print(item, end=' ')
    
    if cont == 2: # Para printar a matéria
        print(f'\n')
        print(f'Matéria: {item}')

    if cont >=3 and cont < 7: # Para printar as notas
        '\n'
        print(f'{cont_bimestre+1}º Bimestre: {item}')
        cont_bimestre += 1

    if cont == 7: # Mostra o total das notas
        '\n'
        print(f'Total: {item}')

    if cont == 7: # Linha separando as matérias
        interface.linha(30)
        cont = 0
        cont_bimestre = 0