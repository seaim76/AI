# Implement DFS using stack, Implement stack using list (append and pop)
def dfs(startingNode, destinationNode):
    reached = [] 
    expand_sequence = []
    frontier = []

    snode = {'City':startingNode,'Path cost':0, 'Path':[startingNode]}
    frontier.append(snode)
    reached.append(startingNode)
    
    while len(frontier) > 0:
        unode = frontier.pop(-1)     
        u = unode['City']
        expand_sequence.append(u)
        if u == destinationNode:
            print(unode)
            print(expand_sequence)
            return unode['Path']
        
        
        for v in romanian_map[u].keys():
            if v not in reached:                
                cost = unode['Path cost'] + romanian_map[u][v] 
                path =  unode['Path'] + [v]
                vnode = {'City': v,'Path cost': cost,'Path': path}
                frontier.append(vnode)
                reached.append(v)
    print('Failed') 