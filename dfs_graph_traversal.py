def dfs_traversal(adj):
    def dfs(node):
        visited[node] = True  # Mark the node as visited
        result.append(node)  # Add to DFS result
        
        # Traverse neighbors in order (as given in adjacency list)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)  # Recursively call DFS

    # Step 1: Initialize required structures
    num_vertices = len(adj)
    visited = [False] * num_vertices  # Track visited nodes
    result = []  # Store DFS traversal

    # Step 2: Start DFS from vertex 0
    dfs(0)
    
    return result  # Return DFS traversal order
