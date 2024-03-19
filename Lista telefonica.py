# dicionarios

telfs = {}
print(telfs)
print(type(telfs))

#adicionar par chave/ valor
telfs['João'] = 2354
telfs['Ana'] = 3456
telfs['Maria'] = 9876
print(telfs)

print(len(telfs))

# listar chaves
for k in telfs.keys():
    print(k)

# testar se a chave existe
print('Ana' in telfs)
print('Nuno' in telfs)

# listar valores
for k in telfs.keys():
    valor = telfs[k]
    print(valor)

# alterar valor
telfs['Maria'] = 7654
print(telfs)

# remover par chave/valor
telfs.pop('Maria')
print(telfs)


#######################
# exercicios

def maximo(lista):
    valor = lista[0]
    for elt in lista:
        if elt > valor:
            valor = elt
    return valor 

lst = [3, 5, 90, 7, -8, 25]
print(maximo(lst))
