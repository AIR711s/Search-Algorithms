from queue import PriorityQueue

graph = {
    "START":[("A",2),("B", 3), ("D", 5)],
    "A":[("C", 4),("START", 2)],
    "B":[("D", 4),("START", 3)],
    "C":[("A", 4),("D", 1),("GOAL", 2)],
    "D":[("START", 5),("B", 4), ("C", 1), ("GOAL", 5)],
    "GOAL":[("C", 2), ("D", 5)],
}

start = "START"
goal = "GOAL"

# UCS -  Lowest Path COST
def UCS_Lowest_cost(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    history = {start: None}
    
    while queue:
        cost, current_state = queue.get()
        visited.add(current_state)
        
        if current_state == goal:
            path = []
            while current_state:
                path.append(current_state)
                current_state = history[current_state]
            
            return path[::-1] 
        
        for neighbour, n_cost in graph[current_state]:
            if neighbour not in visited:
                newCost = cost + n_cost
                queue.put((newCost,neighbour))
                history[neighbour] = current_state 
                
print("Path ", UCS_Lowest_cost(graph, start, goal))