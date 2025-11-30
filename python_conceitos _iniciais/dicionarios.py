#dicionario é uma coleção não ordenada de pares chave e valor
pessoa= {"nome": "Luiz",
         "idade": 30,
         "cidade": "Belo Horizonte"}
#acessando valores por chave
print(pessoa["nome"])

#atibuindo chave
pessoa["sobrenome"]= "Silva"

#alterando chaves já existentes
pessoa["idade"]= 31

#removendo um par chave valor
del pessoa["sobrenome"]

#metodo keys(): retorno de todas as chaves do dicionario em formato de lista
chaves= list(pessoa.keys())
print(chaves[0])

#metodo values(): retorno de todos os valores em formato de lista
valores= list(pessoa.values())
print(valores[0])

#metodo items(): retorno de uma lista de tuplas contendo todos os pares chaves e valores
itens= list(pessoa.items())
print(itens[0][1])
