import networkx, matplotlib.pyplot as plot

# reads = ["TTACGTT", "CCGTTA", "GTTAC", "GTTCGA", "CGTTC"]
reads = ["ATGG"]


def k_mers(seq, k):
    mers = []
    for mer in range (len(seq) - k + 1):
        mers.append(seq[mer : mer + k])
    return mers         


def prefix_suffix(reads, k):
    graph = []
    dic_ = {}
    node = []
    edge = []
    container = []

    for seq in reads:
        k_mer_read = k_mers(seq, k)
        edge.extend(k_mer_read)
        for mer in k_mer_read:
            k_mer = k_mers(mer, k-1)

            
            graph.extend(k_mer)
            for i in graph:
                if i not in container:
                    container.append(i)

    print(edge)

    node = container
    print(node)

    dic_['nodes']=node
    dic_['edges']=edge        

    return dic_


g = (prefix_suffix(reads,3))





def visualizeDBGraph(graph):
    dbGraph = networkx.DiGraph()
    dbGraph.add_nodes_from(graph['nodes']) #Add the nodes to the graph 
    dbGraph.add_edges_from(graph['edges']) #Add the edges to the graph
    networkx.draw(dbGraph, with_labels=True, node_size=1000)
    plot.show()
visualizeDBGraph(g)    
           