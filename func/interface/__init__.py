def titulo(titulo='<none>'):
    tam = len(titulo)

    print('=' * (tam+4))
    print(titulo.center(tam+4).upper())
    print('=' * (tam + 4))


def subTitulo(msg='<none>'):
    tam = len(msg)

    print('-' * (tam+4))
    print(msg.center(tam+4))
    print('-' * (tam + 4))

def linha(tam=0):
    return print('-' * tam)