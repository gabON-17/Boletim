from func.interface import linha
def valida_nota(msg=''): # Valida a nota dos alunos
    while True:
        try:
            nota = float(input(msg))

        except (ValueError,TypeError):       
            print('Valor digitado inválido, digite novamente.')
            linha(15)
        except:
            print('Erro não esperado, tente novamente')
            linha(15)
        else:
            if nota <= 25 and nota >= 0:
                return nota
            else:
                print('Favor digite uma nota de 0 a 25.')
                linha(15)
                continue

def valida_str(msg=''): # Valida uma string para que não tenha caracteres especiais, nem números na str
    while True:
        try:
            string = str(input(msg))

        except (AttributeError, TypeError):
            print(f'{string} não é um nome válido, favor digite um nome válido')
            linha(15)
        else:
            if caractere(string): # Verifica se tem caracteres especiais na str
                print('Caractéres especiais escontrado, favor digite um nome sem caracteres')
                linha(15)
                continue
            
            if len(string) > 30: # Verifica se a str não é mair que 30
                print('ERRO. O nome deve ter no máximo 30 caracteres.')
                linha(15)
                continue
 
            if string.isalnum(): # Verifica se tem números na str 
                cont = 0
                for letra in string:
                    if letra.isnumeric():
                        cont += 1
                        if cont == 1:
                            print('ERRO. Foi encontrado um valor inteiro no seu nome. Tente novamente.')
                            linha(15)
                            continue
            break
    return string


def caractere(str):
    from re import search
    if search(r'[^a-zA-Z0-9\s]', str):
        return True
    else:
        return False