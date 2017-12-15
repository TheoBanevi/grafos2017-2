# -*- coding: cp1252 -*-
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#lista de parentes de cada vertice
parent = {}
#lista das cores de cada veritice
#white o vertice não foi visitado
#gray o vertice foi descoberto
#black o vertice já foi visitado
color = {}
def DFS(G, start):
    global parent,color
    #inicializa as listas com valores nulos e cores brancas
    for i in G.nodes():
        color[i] = 'white'
        parent[i] = None
    #executa o algoritimo de recurssao da DFS
    DFS_visit(G,start)
    #vertices e arestas da DFS-Tree
    nodes = []
    edges = []
    #constroi a DFS-Tree
    for child in parent:
        if parent[child]!= None:
            nodes.append(child)
            edges.append((child, parent[child]))
    #desenha a DFS-Tree
    G2 = nx.Graph()
    G2.add_nodes_from(nodes)
    G2.add_edges_from(edges)
    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2,pos)
    plt.show()

def DFS_visit(G, vert):
    global parent,color
    #o vertice acaba de ser descoberto
    color[vert] = 'gray'
    #para todos os vizinhos do vertice
    for i in G.neighbors(str(vert)):
        #se o vizinho não ter sido visitado
        if color[i] == 'white':
            #o parente do vizinho é o vertice atual
            parent[i]=vert
            #aplicar recurssao com o vizinho
            DFS_visit(G, i)
    #apos passar por todos os vizinhos que nao foram visitados
    #marcar que o veritce atual foi visitado
    color[vert] = 'black'    

def BFS(G, start):
    global parent, color
    #inicializa as listas com valores nulos e cores brancas
    for i in G.nodes():
        color[i]='white'
        parent[i] = None
    #o vertice inicial acaba de ser descoberto
    color[start]= 'gray'
    #pilha de vertices da BFS
    q = []
    #empilha o inicial na pilha de vertices
    q.append(start)
    #enquanto a pilha de vertices nao for vazia
    while q:
        #desempilha o topo da pilha de vertices
        vert = q.pop()
        #para todos os vizinhos do vertice
        for i in G.neighbors(str(vert)):
            #se o vizinho não ter sido visitado
            if color[i] == 'white':
                #o parente do vizinho e o vertice atual
                parent[i]=vert
                #o vizinho acaba de ser descoberto
                color[i]='gray'
                #empilha o vizinho na pilha de vertices
                q.append(i)
        #apos passar por todos os vizinhos que nao foram visitados
        #marcar que o vertice atual foi visitado
        color[vert]='black'
    #vertices e arestas da BFS-Tree
    nodes = []
    edges = []
    #constroi a BFS-Tree
    for child in parent:
        if parent[child]!= None:
            nodes.append(child)
            edges.append((child, parent[child]))
    #desenha a BFS-Tree
    G2 = nx.Graph()
    G2.add_nodes_from(nodes)
    G2.add_edges_from(edges)
    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2,pos)
    plt.show()
    
        
#Desenha o primeiro Grafo original
G = nx.read_pajek('karate.paj')
nx.draw_networkx(G)
plt.show()
#realiza o algoritmo de DFS no primeiro grafo e desenha a DFS-Tree
DFS(G,1)
#realiza o algoritmo de BFS no primeiro grafo e desenha a BFS-Tree
BFS(G,1)
#Desenha o segundo Grafo original
G = nx.read_pajek('dolphins.paj')
nx.draw_networkx(G)
plt.show()
#realiza o algoritmo de DFS no segundo grafo e desenha a DFS-Tree
DFS(G,1)
#realiza o algoritmo de BFS no segundo grafo e desenha a BFS-Tree
BFS(G,1)
