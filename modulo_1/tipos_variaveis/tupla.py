# Tupla é o mesmo que uma lista, porém, IMUTÁVEL
# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla:", minha_tupla)
print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[2]:", minha_tupla[2])
print("Minha tupla[-1]:", minha_tupla[-1])

## Métodos

# Método count()
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# Método index()
indice = minha_tupla.index(3)
print("indice da primeira ocorrência do elemento 3:", indice)