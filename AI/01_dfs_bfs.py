from queue import Queue

class Graph:
    def __init__(self, n:int):
        self.n = n
        self.graph = []
        for i in range(n):
            row = []
            for j in range(n):
                element = int(input(f"Enter distance between node {i} and {j}: "))
                row.append(element)
            self.graph.append(row)

    def print(self):
        for row in self.graph:
            for element in row:
                print(element, end=' ')
            print()
    
    def dfs(self, start:int, visited:list[bool]):
        visited[start] = True
        print(start, end=' ')
        for node in range(len(self.graph[start])):
            if (visited[node] != True and self.graph[start][node] != 0 and self.graph[start][node] != -1):
                self.dfs(node, visited)

    def bfs(self, start:int, visited:list[bool]):
        queue = Queue()
        queue.put(start)
        while (queue.empty() != True):
            node = queue.get()
            if (visited[node] != True):
                visited[node] = True
                print(node, end=' ')
            for neighbour in range(len(self.graph[node])):
                if (visited[neighbour] != True and self.graph[node][neighbour] != 0 and self.graph[node][neighbour] != -1):
                    queue.put(neighbour)
        

if __name__ == "__main__":
    n = int(input("Enter the number of nodes in the graph: "))
    obj = Graph(n)
    visited = []
    for i in range(n):
        visited.append(False)
    choice = int(input("Enter 0 for DFS and 1 for BFS: "))
    if (choice == 0):
        print("DFS sequence is: ")
        obj.dfs(0, visited)
    elif (choice == 1):
        print("BFS sequence is: ")
        obj.bfs(0, visited)
