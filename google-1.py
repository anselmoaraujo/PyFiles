import string

def inverte_minusculas(a):
    entrada = list(a)
    saida = []
    lista_letras = list(string.ascii_lowercase)
    lista_letras_reverse = list(string.ascii_lowercase[::-1])
    for letra in entrada:
        if letra in lista_letras:
            saida.append(lista_letras_reverse[lista_letras.index(letra)])
        else:
            saida.append(letra)
    return saida

inverte_minusculas("wrv blf hvv ozhg mrtsg'h vkrhlwv?")
# >>> 'did you see last night's episode?'