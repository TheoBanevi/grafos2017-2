import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#algoritimo de Prim
def Prim(G, start):
	#define o peso de todos os nós com infinito
    for i in G.nodes():
        G.nodes[i]['weight'] = np.inf
	#Nó inicial recebe peso 0
    G.node[start]['weight'] = 0
	
	#Lista de parentes de um vértice 
    Parent = {}
	
	#inicializa a lsita de parentes com valores vazios
    for i in G.nodes():
        Parent[i] = None
	#Enquanto o fila de prioridades (q) for maior que zero 
    while G.number_of_nodes()>0:
		#define o primeiro peso mínimo como infinito para que o próximo se torne o peso mínimo
        weightMin = np.inf
		#Compara e encontra o vértice de menor peso
        for i in G.nodes():
            if G.nodes[i]['weight'] <= weightMin:
                nodeWeightMin = i
                weightMin = G.node[i]['weight']
		#para todos os vizinhos que tenham o peso minimo
		#compara se a o peso em q é maior que o peso da aresta
		#se for atualiza o peso em q e atualiza atualiza a lista de parentes
        for i in G.neighbors(nodeWeightMin):
            if G.node[i]['weight'] > G.get_edge_data(nodeWeightMin, i)['weight']:
                G.node[i]['weight'] = G.get_edge_data(nodeWeightMin, i)['weight']
                Parent[i] = nodeWeightMin
		#retira o vértice de q
        G.remove_node(nodeWeightMin)
	#vértices e arestas da MST
    nodes = []
    edges = []
	#Cónstroi a MST
    for child in Parent:
	    if Parent[child] != None:
		    nodes.append(child)
		    edges.append((child, Parent[child]))
	#Desenha a MST  (G2)
    G2 = nx.Graph()
    G2.add_nodes_from(nodes)
    G2.add_edges_from(edges)
    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2,pos)
    plt.show()
#Desenha o Grafo original
A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)
nx.draw_networkx(G)
plt.show()
#Realiza o algoritimo de Prim no Grafo original
Prim(G, 1)
