# Coleção não ordenada de chaves, pares e valores

# Criando um dicionário de exemplo
pessoa = {"nome": "Adelmo", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Dias"
print("Sobrenome:", pessoa["sobrenome"])

## Métodos
pessoa["idade"] = 31
print("Nova idade:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Dicionário sem sobrenome:", pessoa)

# keys(): Retorna uma lista de chaves do dicionário
chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)

# values(): Retorna uma lista de valores do dicionário
valores = pessoa.values()
print("Valores do dicionário:", valores)

# list(): Converte uma dict_keys, dict_items ou dict_values em lista Array
print("valores em lista:", list(chaves))

# items(): Retorna uma tupla com chaves e valores
items = list(pessoa.items())
print("Pares chave-valor do dicionário:", items)
print("Primeira chave-valor: %s = %s" % (items[0][0], items[0][1]))