def valida_nota(msg):
    while True:
        try:
            nota = float(input(msg))

        except (ValueError,TypeError):       
            print('Valor digitado inválido, digite novamente.')
            print('-'*15)
        except:
            print('Erro não esperado, tente novamente')
            print('-'*15)
        else:
            if nota <= 25 and nota >= 0:
                return nota
            else:
                print('Favor digite uma nota de 0 a 25.')
                print('-' * 15)
                continue
