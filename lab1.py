import random
import sys
from threading import Thread

from igraph import Graph, plot

vertex_count = int(sys.argv[1])


def draw(graph):

    for es in graph.es:
        es['label'] = es['weight']

    for i, vs in enumerate(graph.vs):
        vs['label'] = i
        vs['color'] = 'gray'

    plot(graph, **{'vertex_size': 40},
         margin=50,
         bbox=(480, 320),
         layout=graph.layout_circle())

def prim(in_graph, out_graph, current_vertex=0, done=[]):

    incident_edges = [in_graph.es[id] for id in in_graph.incident(current_vertex)]   # поиск інцедентних ребер
    incident_edges = list(
        filter(lambda edge: edge.source not in done and
                            edge.target not in done, incident_edges))         # фільтр доданих ребер
    if not incident_edges:                                                    # якщо відсутні - вихід
        return

    min_incident_edge = min(incident_edges, key=lambda edge: edge['weight'])  # ребро з найменшою вагою

    out_graph.add_edge(source=min_incident_edge.source,                       # додати ребро у новий граф
                       target=min_incident_edge.target,
                       weight=min_incident_edge['weight'])

    next_vertex = min_incident_edge.target \
        if min_incident_edge.target != current_vertex \
        else min_incident_edge.source                                         # наступна вершина - один з кінців ребра

    done.append(current_vertex)   # відмітити пройдену вершину
    prim(in_graph, out_graph, next_vertex, done)        # рекурсивно дивись в наступну вершину

source = Graph.Full(vertex_count)    # створює зв’язаний граф з вказаною кількістю вершин

for es in source.es:
    es['weight'] = random.randint(1, 9)

min_ost = Graph(vertex_count)

prim(source, min_ost)

Thread(target=lambda: draw(source)).start()
Thread(target=lambda: draw(min_ost)).start()
