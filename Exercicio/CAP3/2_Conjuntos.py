# Exercicio 2

loja1 = {'s21','s22','s23','iphone 13', 'iphone 12','a70'}
loja2 = {'s23 plus', 's23','iphone x','iphone 12','a70'}

todas_opcoes = loja1 | loja2
print(todas_opcoes)

mesmo_modelo = loja1 & loja2
print(mesmo_modelo)