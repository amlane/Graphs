"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: Vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        s = Stack()
        # add the starting vertex_id to the queue
        s.push(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # while the queue is not empty...
        while s.size() > 0:
            # dequeue the first vertex
            v = s.pop()
            # check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        results = Stack()
        visited = set()

        def dft(start):
            # BASE CASE: if there is no start
            if start is None:
                # return
                return
            # add start to results stack
            results.push(start)
            # mark vertex as visited
            v = results.pop()
            if v not in visited:
                print(v)
                visited.add(v)
            # for each neighbor in vertex's neighbor
            for neighbor in self.get_neighbors(v):
                # if neighbor is not visited
                if neighbor not in visited:
                    # recursively call function on neighbor
                    dft(neighbor)
        dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            v = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            current_node = v[-1]
            # CHECK IF IT'S THE TARGET
            if current_node == destination_vertex:
                # IF SO, RETURN THE PATH
                return v
            # Check if it's been visited
            # If it has not been visited...
            if current_node not in visited:
                # Mark it as visited
                visited.add(current_node)
            # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(current_node):
                    # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding the neighbor)
                    path_copy = list(v)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue
        s = Stack()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue, the first PATH
            v = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            current_node = v[-1]
            # CHECK IF IT'S THE TARGET
            if current_node == destination_vertex:
                # IF SO, RETURN THE PATH
                return v
            # Check if it's been visited
            # If it has not been visited...
            if current_node not in visited:
                # Mark it as visited
                visited.add(current_node)
            # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(current_node):
                    # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding the neighbor)
                    path_copy = list(v)
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited if it's not yet initialized
        if visited is None:
            visited = set()
        # initialize path if it's not yet initialized
        if path is None:
            path = list()
        # Check if starting vertex has been visited
        if starting_vertex not in visited:
            # if not...
            # mark it as visited
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # if starting_vertex == destination_vertex
            if starting_vertex == destination_vertex:
                # return path
                return path_copy
            # Call DFS recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print("")
    print("*****************************")
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("")
    print("*****************************")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("")
    print("*****************************")
    graph.dft_recursive(1)
    print("")
    print("*****************************")
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
