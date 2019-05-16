# Search methods

import search
caminos = [['A','F','V','I'],['B','Z','R','Z']]

for i in range(0,4):
    print("Ruta de ", caminos[0][i]," --> ", caminos[1][i],end="\n \n")
    camino=search.GPSProblem(caminos[0][i],caminos[1][i],search.romania)
    print("\nAnchura : ")
    print(search.breadth_first_graph_search(camino).path())
    print("\nProfundidad: ")
    print(search.depth_first_graph_search(camino).path())
    print("\nRamificacion y acotacion: ")
    print(search.branch_and_bound(camino).path())
    print("\nRamificacion y acotacion con subestimacion: ")
    print(search.branch_and_bound_subestimation(camino).path())
    print("\n-----------------------\n")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
