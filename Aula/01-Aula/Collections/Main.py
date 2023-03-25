''' COLEÇÕES PYTHON '''

# 1 - Tupla (coleção imutavél)
# nomes = ('goku', 'vegeta', 'trunks', 'gohan')
# print(nomes)
# nomes[0] = 'kuririn'

''' ----------------------------------------------------- '''

# # 2 - Lista
# nomes = ['goku', 'vegeta', 'trunks', 'gohan']
# print(type(nomes))
# print(nomes)
# # Insert
# nomes.append('kuririn')
# # Update
# nomes[0] = 'pan'
# # Delete
# nomes.pop(1)
# nomes.remove('trunks')
# print(nomes)

# # Slicing (recortar/fatiar)
# # Ele vai pegar os dados do indice 1 para frente
# # O primeiro valor é inclusive, o ultimo é exclusivo
# print(nomes[1:])

''' ----------------------------------------------------- '''

# # 3 - Conjuntos (não repete elementos/ não guarda indice/ sem update)
# nomes = {'goku', 'vegeta', 'trunks', 'gohan'}
# print(nomes)
# # Insert
# nomes.add('piccolo')
# # Remove
# nomes.remove('trunks')
# print(nomes)

''' ----------------------------------------------------- '''

# # 4 - Dicionário (indices cutomizáveis/ chave - valor)
# pessoa1 = {
#             'nome':'goku', 
#             'idade': 30
#         }
# pessoa2 = {
#             'nome':'gohan', 
#             'idade': 12
#         }
# pessoas = []
# pessoas.append(pessoa1)
# pessoas.append(pessoa2)
# print(pessoas[1]['idade'])
