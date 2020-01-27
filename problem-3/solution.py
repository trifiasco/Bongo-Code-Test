
class node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def get_parents(current_node, parents = []):
    parents.append(current_node)
    
    if current_node.parent is None:
        return parents
    return get_parents(current_node.parent, parents)


    

def solve_lca(nodes_map, node1_value, node2_value):
    parents_of_node1 = get_parents(nodes_map[node1_value], [])
    parents_of_node2 = get_parents(nodes_map[node2_value], [])

    parents_of_node1.reverse()
    parents_of_node2.reverse()

    iterator = 0

    while iterator < len(parents_of_node1) and iterator < len(parents_of_node2) :
        if parents_of_node1[iterator].value != parents_of_node2[iterator].value:
            break
            
        iterator += 1

    print(parents_of_node1[iterator - 1].value)

if __name__ == '__main__':
    
    # sample input preparation
    #this block will prepare the tree given in the pdf
    nodes_map = dict()
    root_node = None
    for i in range(1, 10, 1):
        parent_node_value = i // 2
        parent_node = None
        if parent_node_value in nodes_map:
            parent_node = nodes_map[parent_node_value]

        current_node = node(i, parent_node)
        if parent_node == None:
            root_node = current_node
        nodes_map[i] = current_node

    # now call solve method with arbitrary pair of nodes
    solve_lca(nodes_map, 6, 7)
    solve_lca(nodes_map, 3, 7)
    solve_lca(nodes_map, 8, 6)