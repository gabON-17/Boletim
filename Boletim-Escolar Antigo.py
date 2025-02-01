from time import sleep

print('-='*20)
print(' '*10, 'BOLETIM ESCOLAR')
print('-='*20)

sleep(2)

print('Vamos pegar algumas informações para que seu boletim seja feito!')

matriz = [[]] # Matriz Responsável por guardar as notas e as matérias
 
cont = 1 # Conntador do Programa (Utilizado em várias parte do programa)
matriz_cont = 0 # Contador da matriz 

while True:
    
    print('-'*35)
    
    materias = str(input(f'Digite sua {cont}° matéria [0 para parar]: ')) # Coleta as Matérias do usuário

    if materias == '0':
        break

    if matriz_cont == len(matriz): # Se não tiver mais espaço para as matérias ele criará um
        matriz.append([])

    matriz[matriz_cont].append(materias)

    cont += 1
    matriz_cont += 1

print('-='*35)
print('Otímo, agora preciso das suas notas em cada BIMESTRE')
print('-='*35)

matriz_cont = 0

for m in matriz: # Para cada m(materia) em matriz
    
    soma = 0 # Soma as notas e vale 0 toda vez que troca de matéria

    m = ' '.join(m) # Tira de LISTA e coloca como uma STR 

    for c in range(1, 5): 

       

        notas = float(input(f'Digite sua nota no {c}° bimestre em {m}: ')) # Pega o valor das notas
        print('-'*30)
        
        if notas > 25 or notas < 0: # Condição para caso a nota do BIMESTRE seja maior que 25
             
            while notas > 25 or notas < 0:
                notas = float(input('ERRO! Nota máxima permitida por bimestre é 25, Tente novamente: '))
                print('-'*30)

        soma += notas 

        matriz[matriz_cont].append(notas) # ADICIONA as notas na matriz

        if c == 4:
            matriz[matriz_cont].append(soma) # Adiciona a soma total dos bimestre ao final da matriz 
            matriz_cont += 1 # Adiciona 1 no contador de matriz

print('-='*40)
print('Aguarde...')
sleep(5)

matriz_cont = 0 # Para pegar a lista da matriz

while matriz_cont < len(matriz):

    materia = matriz [matriz_cont] [0] # PEGA as matérias do usuário separadamente
    total = matriz[matriz_cont] [5] # PEGA o total de cada matéria
       
    print(str(f'{' '*5} {materia}' ).upper())
                                                    
    for c in range(1, 5): # MOSTRAR os bimestres

        print()
        
        bimestre = matriz [matriz_cont] [c]

        print(f' {' '*5} {c}° BIMESTRE : {bimestre}')
    
    print()

    print(f'{' '*5} TOTAL == {total} ', end='>'*3)

    if total >= 60: # Condição SE o aluno passou naquela matéria
        print(' Você Passou!!')

    else:
        print(' Você Não Passou!')

    sleep(5)
    
    print('-='*30)

    matriz_cont += 1

print('FIM!')
