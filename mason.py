import networkx as nx


def calcular_ganho_caminho(caminho, G):
    ganho = 1
    for i in range(len(caminho) - 1):
        ganho *= G.edges[caminho[i], caminho[i + 1]]['weight']
    return ganho


def calcular_ganho_ciclo(ciclo, G):
    ganho = 1
    # Garante que o ciclo esteja fechado para cálculo correto
    ciclo_fechar = ciclo + [ciclo[0]]
    for i in range(len(ciclo_fechar) - 1):
        ganho *= G.edges[ciclo_fechar[i], ciclo_fechar[i + 1]]['weight']
    return ganho


def encontrar_todos_ciclos(G):
    ciclos = list(nx.simple_cycles(G))
    # Filtra ciclos com mais de um nó
    return [ciclo for ciclo in ciclos if len(ciclo) > 1]


def calcular_delta(G, ciclos):
    from sympy import expand
    delta = 1
    soma_ganho_ciclos = sum(calcular_ganho_ciclo(ciclo, G) for ciclo in ciclos)
    delta -= soma_ganho_ciclos
    return expand(delta)


def main():
    G = nx.DiGraph()
    G.add_edge('Entrada', 'A', weight=2)
    G.add_edge('A', 'B', weight=3)
    G.add_edge('B', 'Saída', weight=5)
    G.add_edge('B', 'C', weight=-1)
    G.add_edge('C', 'A', weight=-1)
    G.add_edge('A', 'D', weight=4)
    G.add_edge('D', 'Saída', weight=2)

    caminhos = list(nx.all_simple_paths(G, source='Entrada', target='Saída'))
    ciclos = encontrar_todos_ciclos(G)
    delta = calcular_delta(G, ciclos)

    ganho_total = 0
    for caminho in caminhos:
        ganho_caminho = calcular_ganho_caminho(caminho, G)
        ciclos_nao_tocantes = [ciclo for ciclo in ciclos if not set(
            ciclo).intersection(set(caminho))]
        delta_caminho = calcular_delta(G, ciclos_nao_tocantes)
        ganho_total += ganho_caminho / delta_caminho

    print(f"O ganho total de Entrada para Saída é: {ganho_total}")


if __name__ == "__main__":
    main()


''' Explicação dos Comentários Adicionados:
calcular_ganho_caminho: Esta função recebe um caminho e o grafo como argumentos
    e calcula o ganho multiplicando os pesos das arestas que compõem o caminho.

calcular_ganho_ciclo: Similar à função de caminho, mas para ciclos, 
    calculando o produto dos pesos das arestas que formam um ciclo.

encontrar_todos_ciclos: Usa a biblioteca NetworkX para encontrar todos 
    os ciclos simples no grafo, essencial para calcular o Δ.

calcular_delta: Calcula o determinante do sistema, que é usado na 
    fórmula de Mason para determinar o ganho total do sistema.

main: A função principal configura o grafo, identifica caminhos e ciclos, 
    calcula o delta e, finalmente, usa as regras de Mason para calcular o ganho total do sistema de Entrada para Saída.'''
