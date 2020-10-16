import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
 #initialising the graph
G = nx.Graph()
nodes=["Sports Complex","Siwaka","Ph.1A","Ph.1B","Mada","STC","Phase 2","Phase 3","J1","Parking Lot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("Sports Complex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Ph.1B","Phase 2",weight="112")
G.add_edge("Phase 2","STC",weight="50")
G.add_edge("Phase 2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Phase 2","Phase 3",weight="500")
G.add_edge("STC","Parking Lot",weight="250")
G.add_edge("Mada","Parking Lot",weight="700")
G.add_edge("Phase 3","Parking Lot",weight="350")

#position the nodes to resemble the map
G.nodes["Sports Complex"]['pos']=(-8,4)
G.nodes["Siwaka"]['pos']=(-4,4)
G.nodes["Ph.1A"]['pos']=(0,4)
G.nodes["Ph.1B"]['pos']=(0,0)
G.nodes["STC"]['pos']=(0,-4)
G.nodes["Phase 2"]['pos']=(4,0)
G.nodes["Phase 3"]['pos']=(8,-4)
G.nodes["J1"]['pos']=(8,0)
G.nodes["Mada"]['pos']=(12,0)
G.nodes["Parking Lot"]['pos']=(8,-8)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"Sports Complex","Parking Lot")
print(route_bfs.visited)
route_list = route_bfs.visited

#color the nodes in the route_bfs
node_col = ['#CC99FF' if not node in route_list else '#FF6666' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
nx.draw_networkx(G, node_pos,node_color= node_col,node_size=1000)
nx.draw_networkx_edges(G, node_pos,width=2)

#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()