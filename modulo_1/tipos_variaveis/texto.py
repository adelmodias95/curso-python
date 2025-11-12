# Declaração
nome_completo = "Adelmo Dias"

nome_completo_aspas = """Adelmo
Moura"""

nome_completo_quebra = "Adelmo \
Moura"

nome = "Adelmo"
sobrenome = "Dias"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Adelmo" + "Dias")
print("Nome completo (4a forma): " + "Adelmo", "Dias")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))