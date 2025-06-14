import matplotlib.pyplot as plt
import numpy as np
import time
from search import aStarSearch, breadthFirstSearch, depthFirstSearch, uniformCostSearch
from searchAgents import FoodSearchProblem

def coletar_estatisticas(problema, algoritmo, nome_algoritmo):
    """Coleta estatísticas de um único algoritmo de busca"""
    inicio = time.time()
    caminho = algoritmo(problema)
    fim = time.time()
    
    stats = {
        'tempo': (fim - inicio) * 1000,  # ms
        'nos_expandidos': problema._expanded,
        'tamanho_caminho': len(caminho)
    }
    
    print(f"\n{nome_algoritmo}:")
    print(f"Tempo: {stats['tempo']:.2f}ms")
    print(f"Nós expandidos: {stats['nos_expandidos']}")
    print(f"Tamanho do caminho: {stats['tamanho_caminho']}")
    return stats

def comparar_algoritmos(problema):
    """Compara os algoritmos de busca"""
    import search # Importação local para evitar ciclo
    
    algoritmos = [
        (search.aStarSearch, "A*"),
        (search.breadthFirstSearch, "BFS"), 
        (search.depthFirstSearch, "DFS"),
        (search.uniformCostSearch, "UCS")
    ]
    
    resultados = {}
    for alg, nome in algoritmos:
        print(f"\nTestando {nome}...")
        resultados[nome] = coletar_estatisticas(problema, alg, nome)
    
    print("\nComparação Final:")
    print("-" * 50)
    print(f"{'Algoritmo':<10} {'Tempo(ms)':<12} {'Nós':<8} {'Caminho'}")
    print("-" * 50)
    
    for nome, stats in resultados.items():
        print(f"{nome:<10} {stats['tempo']:<12.2f} {stats['nos_expandidos']:<8} {stats['tamanho_caminho']}")
