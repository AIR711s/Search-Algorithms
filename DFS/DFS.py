from collections import deque

graph = {
    "START":["A","B", "D"],
    "A":["C","START"],
    "B":["D","START"],
    "C":["A","D","GOAL"],
    "D":["START","B", "C", "GOAL"],
    "GOAL":["C", "D"],
}

start = "START"
goal = "GOAL"

# BFS- shortest Path
def DFS(graph, start, goal):
    queue = deque([start])
    visited = set()
    history = {start: None}
    
    # LIFO 

    while queue:
        current_state = queue.pop()
        visited.add(current_state)
        
        if current_state == goal:
            path = []
            while current_state:
                path.append(current_state)
                current_state = history[current_state]
            
            return path[::-1] 
        
        for neighbour in graph[current_state]:
            if neighbour not in visited:
                queue.append(neighbour)
                history[neighbour] = current_state 
                # {"A": "START"} 
                # {"B": "START"} 
                # {"D": "START"} 
                
print("Path ", shortest_path(graph, start, goal))