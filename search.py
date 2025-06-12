# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Implementa o algoritmo de busca em profundidade (DFS).
    Retorna uma lista de ações que leva do estado inicial ao objetivo.
    """
    # Inicializa estruturas de dados
    fronteira = util.Stack()                     # Pilha para fronteira de busca
    visitados = set()                            # Conjunto para estados visitados
    fronteira.push((problem.getStartState(), [])) # Tupla (estado, ações)

 

    while not fronteira.isEmpty():
        estado_atual, acoes = fronteira.pop()
        
        # Verifica se chegou ao objetivo
        if problem.isGoalState(estado_atual):
            return acoes
            
        # Explora sucessores se estado não foi visitado
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            
            # Adiciona sucessores não visitados à pilha
            for sucessor, acao, custo in problem.getSuccessors(estado_atual):
                if sucessor not in visitados:
                    novas_acoes = acoes + [acao]
                    fronteira.push((sucessor, novas_acoes))
    
    return [] # Retorna lista vazia se não encontrar solução


def breadthFirstSearch(problem):
    """
    Implementa o algoritmo de busca em largura (BFS).
    Retorna uma lista de ações que leva do estado inicial ao objetivo.
    """
    # Inicializa estruturas de dados
    fronteira = util.Queue()                     # Fila para fronteira de busca
    visitados = set()                            # Conjunto para estados visitados
    fronteira.push((problem.getStartState(), [])) # Tupla (estado, ações)
    visitados.add(problem.getStartState())       # Marca estado inicial como visitado

    while not fronteira.isEmpty():
        estado_atual, acoes = fronteira.pop()
        
        # Verifica se chegou ao objetivo
        if problem.isGoalState(estado_atual):
            return acoes
            
        # Explora todos os sucessores
        for sucessor, acao, custo in problem.getSuccessors(estado_atual):
            if sucessor not in visitados:
                visitados.add(sucessor)          # Marca sucessor como visitado
                novas_acoes = acoes + [acao]     # Adiciona ação ao caminho
                fronteira.push((sucessor, novas_acoes))
    
    return [] # Retorna lista vazia se não encontrar solução

def uniformCostSearch(problem):
    """
    Implementa o algoritmo de busca de custo uniforme (UCS).
    Retorna uma lista de ações que leva do estado inicial ao objetivo com menor custo.
    """
    # Inicializa estruturas de dados
    fronteira = util.PriorityQueue()                   # Fila de prioridade por custo
    visitados = set()                                  # Conjunto de estados visitados
    fronteira.push((problem.getStartState(), [], 0), 0)  # (estado, ações, custo_total), prioridade

    while not fronteira.isEmpty():
        estado_atual, acoes, custo_atual = fronteira.pop()
        
        # Se o estado atual não foi visitado
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            
            # Verifica se chegou ao objetivo
            if problem.isGoalState(estado_atual):
                return acoes
            
            # Explora sucessores
            for sucessor, acao, custo in problem.getSuccessors(estado_atual):
                if sucessor not in visitados:
                    novo_custo = custo_atual + custo
                    novas_acoes = acoes + [acao]
                    fronteira.push((sucessor, novas_acoes, novo_custo), novo_custo)
    
    return [] # Retorna lista vazia se não encontrar solução

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Implementa o algoritmo de busca A*.
    Usa g(n) + h(n) como prioridade, onde:
    g(n) = custo até o nó atual
    h(n) = valor da heurística para o nó atual
    """
    fronteira = util.PriorityQueue()
    visitados = set()
    inicio = problem.getStartState()
    fronteira.push((inicio, [], 0), 0)  # (estado, ações, g(n))

    while not fronteira.isEmpty():
        estado_atual, acoes, custo_g = fronteira.pop()
        
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            
            if problem.isGoalState(estado_atual):
                return acoes
                
            for sucessor, acao, custo in problem.getSuccessors(estado_atual):
                if sucessor not in visitados:
                    novo_g = custo_g + custo
                    novo_h = heuristic(sucessor, problem)  # Valor da heurística
                    prioridade = novo_g + novo_h          # f(n) = g(n) + h(n)
                    novas_acoes = acoes + [acao]
                    fronteira.push((sucessor, novas_acoes, novo_g), prioridade)
    
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
