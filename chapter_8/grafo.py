infinito = float('inf')
grafo = {}

grafo['inicio'] = {}
# grafo['inicio']['a'] = 5
# grafo['inicio']['b'] = 2
grafo['inicio']['a'] = 10

grafo['a'] = {}
# grafo['a']['c'] = 4
# grafo['a']['d'] = 2
grafo['a']['b'] = 20

grafo['b'] = {}
# grafo['b']['a'] = 8
# grafo['b']['d'] = 7
grafo['b']['c'] = 1
grafo['b']['fim'] = 30

grafo['c'] = {}
# grafo['c']['d'] = 6
# grafo['c']['fim'] = 3
grafo['c']['a'] = 1

# grafo['d'] = {}
# grafo['d']['fim'] = 1

grafo['fim'] = {}

custos = {}
# custos['a'] = 5
custos['a'] = 10
# custos['b'] = 2
custos['c'] = infinito
custos['b'] = infinito
custos['fim'] = infinito

pais = {}
pais['a'] = 'inicio'
pais['b'] = None
pais['c'] = None
# pais['d'] = None
# pais['fim'] = None

processados = []

def get_custo_mais_baixo(custos):
  custo_mais_baixo = float('inf')
  nodo_mais_baixo = None
  
  for nodo in custos:
    if custos[nodo] < custo_mais_baixo and nodo not in processados:
      custo_mais_baixo = custos[nodo]
      nodo_mais_baixo = nodo
  
  return nodo_mais_baixo

nodo = get_custo_mais_baixo(custos)
while nodo is not None:
  custo = custos[nodo]
  vizinhos = grafo[nodo]
  for n in vizinhos.keys():
    novo_custo = custo + vizinhos[n]
    if custos[n] > novo_custo:
      custos[n] = novo_custo
      pais[n] = nodo
  processados.append(nodo)
  nodo = get_custo_mais_baixo(custos)

print custos['fim']