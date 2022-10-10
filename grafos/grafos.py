import networkx as nx  # Networkx para grafos
import pandas as pd  # Pandas para importar datos
import matplotlib.pyplot as plt  # Mathplotlib para graficar


def grafos():
    nodos = pd.read_csv('Estados.csv', sep=';')
    print(nodos.head())
    print(nodos.tail())
    print(nodos.loc[3])
    print(nodos['Code'])
    nodos.set_index(["Code"], inplace=True)
    print(nodos.head())
    print(nodos.loc['DL'])
    # %% Arcos - arista
    arcos = pd.read_csv('Conexiones.csv', sep=';')
    print(arcos.head(7))
    print(arcos.describe())
    print(arcos.corr())

    # %% Creando el grafo
    G = nx.from_pandas_edgelist(arcos, "E1", "E2", ["Km", "Costo"])
    print(G.nodes())  # muestra la lista de nodos
    print(G.order())  # retornar el orden
    print(G.edges())  # muestra la lista de aristas
    print(G.size())  # Tamaño del grafo
    print(G.has_node('AY'))
    print(G.has_node('AX'))

    # %%Graficando
    plt.rcParams['figure.figsize'] = (10.0, 10.0)
    plt.figure()
    nx.draw_spring(G,
                   node_color="lightblue",
                   edge_color="blue",
                   font_size=18,
                   width=2, with_labels=True, node_size=2500)

    # %%Obteniendo camino más corto _ Rutas
    # General
    camino = list(nx.all_shortest_paths(G, source='NK', target='CD'))
    print('Caminos más cortos: \n', camino)
    # Dijkstra
    cdk1 = list(nx.dijkstra_path(G, source='NK', target="CD", weight='Km'))
    print('Camino por algoritmo dijkstra KM: \n', cdk1)
    cdk2 = list(nx.dijkstra_path(G, source='NK', target="CD", weight='Costo'))
    print('Camino por algoritmo dijkstra $: \n', cdk2)
    # A*
    as1 = list(nx.astar_path(G, ('NK'), ('CD'), weight="Km"))
    print('Camino por algoritmo A* KM: \n', as1)
    as2 = list(nx.astar_path(G, ('NK'), ('CD'), weight="Costo"))
    print('Camino por algoritmo A* $: \n', as2)

    # %% Mostrando la ruta e información de interés
    def ver_ruta(ruta):  # método
      total_km = 0
      total_costo = 0
      print('Descripción de la ruta: ')
      for i in range(len(ruta)-1):
        origen = ruta[i]
        destino = ruta[i+1]
        Km = G[origen][destino]['Km']
        costo = G[origen][destino]['Costo']
        total_km += Km
        total_costo += costo
        print(nodos.loc[origen]['Node'], '->', nodos.loc[destino]['Node'],
        ': distancia en Km: ', Km,
        ', costo del trayecto $: ', costo)
      print('Duración total: ', total_km, ' Km',
      ', Costo total:', total_costo, '$')
      print('..........................................')
    ver_ruta(as1)  # Selección por Km
    ver_ruta(as2)  # Selección por Costo

  # %% Graficando la ruta
"""def plot_ruta(ruta): #Método de graficación
    posi = nx.circular_layout(G) #posición para graficación
    nx.draw(G, pos=posi, #grafo principal
    node_color='lightblue',
    edge_color='blue',
    font_size=20,
    width=2, with_labels=True, node_size=3500, alpha=0.8)
    subG=nx.Graph() #Grafo auxiliar con la ruta escogida
    for i in range(len(ruta)-1):
      subG.add_edge(ruta[i], ruta[i+1])
    
    nx.draw(subG, pos=posi, #ruta
        node_color='dodgerblue',
        edge_color='red',
        font_size=20,
        width=3, with_labels=True, node_size=3000
      )
    plt.show()
      
  plt.figure() #nueva figura
  plot_ruta(as1) #graficando ruta
 """
if __name__ == "__main__":
    grafos()
