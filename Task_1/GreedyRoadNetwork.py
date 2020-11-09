import os
import networkx as nx
import matplotlib.pyplot as plt
from classes.greedy import GreedyTraverser

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","Phase3","J1","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka" ,distance=450)
G.add_edge("Siwaka","Ph.1A",distance=10)
G.add_edge("Siwaka","Ph.1B",distance=230)
G.add_edge("Ph.1A","Ph.1B",distance=100)
G.add_edge("Ph.1A","Mada",distance=850)
G.add_edge("Ph.1B","Phase2",distance=112)
G.add_edge("Ph.1B","STC",distance=50)
G.add_edge("STC","Phase2", distance=50)
G.add_edge("STC","ParkingLot",distance=250)
G.add_edge("Phase2","Phase3",distance=500)
G.add_edge("Phase3","ParkingLot", distance=350)
G.add_edge("Phase2","J1", distance=600)
G.add_edge("J1","Mada",distance=200)
G.add_edge("Mada","ParkingLot", distance=10)

#position the nodes to resemble the map
G.nodes["SportsComplex"]['pos']=(-8,4)
G.nodes["Siwaka"]['pos']=(-4,4)
G.nodes["Ph.1A"]['pos']=(0,4)
G.nodes["Ph.1B"]['pos']=(0,0)
G.nodes["STC"]['pos']=(0,-4)
G.nodes["Phase2"]['pos']=(4,0)
G.nodes["Phase3"]['pos']=(8,-4)
G.nodes["J1"]['pos']=(8,0)
G.nodes["Mada"]['pos']=(12,0)
G.nodes["ParkingLot"]['pos']=(8,-8)
#store all positions in a variable

def getHeuristics(G):
    heuristics = {}
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, 'heuristics.txt'))
    for i in G.nodes():
        node_heuristic_val = f.readline().split()
        heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
    return heuristics

heuristics = getHeuristics(G)
node_pos = nx.get_node_attributes(G,'pos')

#call BFS to return set of all possible routes to the goal
route_bfs = GreedyTraverser()
routes = route_bfs.Greedy(G,heuristics,"SportsComplex","ParkingLot")


route_list = route_bfs.path
#color the nodes in the route_bfs
node_col = ['#CC99FF' if not node in route_list else '#FF6666' for node in G.nodes()]

peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['#CC99FF' if not edge in peru_colored_edges else '#FF6666' for edge in G.edges()]

arc_label=nx.get_edge_attributes(G,'label')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=5,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_label)
#nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels={('SportsComplex','Siwaka'):'UnkRoad450m',
   ('Siwaka','Ph.1A'):'SangaleRd10m',('Siwaka','Ph.1B'):'SangaleLink230m',('Ph.1A','Ph.1B'):'ParkingWalkWay100m',('Ph.1B','Phase2'):'KeriRd112m',
   ('Phase2','J1'):'KeriRd600m',('J1','Mada'):'SangaleRd200m',('Ph.1A','Mada'):'SRd850m',('Ph.1B','STC'):'KeriRd50m',
   ('STC','Phase2'):'STCwalkway50m',('Phase2','Phase3'):'KeriRd500m',('Phase3','ParkingLot'):'HGRd350m',('STC','ParkingLot'):'LibraryWalkWay250m',
   ('ParkingLot','Mada'):'LangataRd700m'},font_color='orange',font_size='x-small')
plt.axis('off')