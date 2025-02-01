 # Criar um programa onde pegue as matérias e as notas e crie um boletim escolar.
from time import sleep

cont = 1 # CONTADOR
lista_notas = []
lista_materias = [] 

# DADOS MATERIAS
var_quant_materias = int(input('Quantas matérias você possui? ')) # Quantidade de matérias

while var_quant_materias >= cont: # Enquanto quant_materias for maior ou igual ao contador
    
    var_materias = str(input(f'Qual a {cont}° matéria? '))

    lista_materias.append(var_materias) # Pega a os valores digitados em var_materias e salva na lista_materias

    cont = cont + 1

print('-='*30)
print('Otímo! Agora preciso saber suas notas!')
print('-='*30)

sleep(1) # Adiciona um atraso de 1 segundo

# DADOS NOTAS

for materia in lista_materias: # Pega um valor da lista de cada vez

    var_notas = float(input(f'Digite sua nota em {materia}: ')) # Mostra um valor da lista_materias de cada vez

    lista_notas.append(var_notas)

print('Muito Obrigado Pelas Informações!!', end=' ')
print('Calculando....')

sleep(2)

print('-='*20)
print('Aqui está seu boletim')

cont = 0 # Usado para definir qual str da lista será utilizado
for notas in lista_notas:

    print('-'*20)
    print(f'{lista_materias[cont]} : {notas}')
    
    cont = cont + 1
print('-='*20)