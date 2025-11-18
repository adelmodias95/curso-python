## Declaração
minha_lista = [1, 2, 3, 4, 5, "python", True, False]

# Exibindo a lista
print("Minha lista:", minha_lista)

# Exibindo um item específico
print("Item 1:", minha_lista[0])

# Exibindo o elemento "python"
print("Elemento python:", minha_lista[5])

# Fatiamento
print("Fatiamento:", minha_lista[0:3])
print("Fatiamento:3", minha_lista[:5])

## Métodos de lista
# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após o append(6):", minha_lista)

# Método index(): retorna o índice do elemento
indice = minha_lista.index(6)
print("index(6)", indice)

# Método insert(): Insere um elemento em um índice específico
minha_lista.insert(1, "index 1")
print("Após o insert:", minha_lista)

# Método pop(): remove o elemento de um index específicado
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove(): remove o elemento de um index específicado
minha_lista.remove("index 1")
print("Após o remove(True):", minha_lista)

# Método sort(): Ordena uma lista de números em ordem crescente
minha_lista = []
minha_lista = [4, 5, 7, 1, 2, 8, 9, 3, 6]
minha_lista.sort()
print("minha nova lista:", minha_lista)