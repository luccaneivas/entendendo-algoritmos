// Conjunto de estados a serem cobertos
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

// Hash com cada estação e o conjunto de estados que a estação cobre
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

// conjunto para armazenar as estações
estacoes_final = set()

// loop para definir as estações que cobrem a maior área possível
while estados_abranger:
  melhor_estacao = None
  estados_cobertos = set()
  
  for estacao, estados_por_estacao in estacoes.items():
    // é feita a intersecção entre os dois conjuntos para definir quais estados são cobertos por essa estação
    cobertos = estados_abranger & estados_por_estacao
    if len(cobertos) > len(estados_cobertos):
      melhor_estacao = estacao
      estados_cobertos = cobertos
  
  estados_abranger -= estados_cobertos
  estacoes_final.add(melhor_estacao)

print estacoes_final