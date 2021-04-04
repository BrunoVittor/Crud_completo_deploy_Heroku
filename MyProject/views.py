from django.http import HttpResponse


def nomes(nome):
    nomepessoas = [
        {'nome': 'Bruno', 'idade': 34},
        {'nome': 'Kamila', 'idade': 30},
        {'nome': 'Isabella', 'idade': 25},
    ]

    for item in nomepessoas:
        if item['nome'] == nome:
            return item
    else:
        return ('pessoa não encontrada')


def pessoas(request, nome):
    nome = nomes(nome)
    if nome['idade'] > 0:
        return HttpResponse('Pessoa encontrada, ela tem ' + str(nome['idade']))
    else:
        return HttpResponse('Pessoa não encontrada')
