from func import mysql, dados, interface
#  Ler as matérias do usuário e mostrar o boletim do aluno
cont_id_mat = 0
notas = list()

interface.titulo('meu boletim')

aluno = dados.valida_str('Digite seu nome: ') # Pega o nome do aluno 
mysql.com_sql(f'insert into alunos values (default, "{aluno}")') # Registra o aluno no banco

materias = mysql.tabela('select nome from materias') # Tem todas as matérias presente no banco de dados
id_mat = mysql.tabela('select id_materia from materias')
id_aluno = mysql.tabela('select id_aluno from alunos')

interface.subTitulo('Digite sua notas')

for valor in materias:
        tot_notas = 0
        for c in range(0, 4):
            nota = dados.valida_nota(f'{c+1} Bimestre em {valor}: ')
            notas.append(nota)

            tot_notas += nota

            if c == 3:
                notas.append(tot_notas)
                mysql.com_sql(f'insert into notas values (default, "{id_aluno[-1]}", "{id_mat[cont_id_mat]}", "{notas[0]}", "{notas[1]}", {notas[2]}, "{notas[3]}", "{notas[4]}" )')
                cont_id_mat += 1
                notas.clear()

        interface.linha(15)
