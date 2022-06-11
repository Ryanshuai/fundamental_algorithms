class Edge:
    def __init__(self, to_vertex, flow, capacity, reversed_edge=None):
        self.to_vertex = to_vertex
        self.flow = flow
        self.capacity = capacity
        self.reversed_edge = reversed_edge


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [list() for _ in range(n)]
        self.level = [-1] * n
        self.m = 0
        self.debug_edge = []

    def add_edge(self, u, v, capacity):
        a = Edge(v, 0, capacity)
        b = Edge(u, 0, capacity, a)
        a.reversed_edge = b
        self.adj[u].append(a)
        self.adj[v].append(b)
        self.m += 1
        self.debug_edge.append((u, v, capacity))

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for edge in self.adj[u]:
                if edge.capacity > edge.flow and self.level[edge.to_vertex] < 0:
                    self.level[edge.to_vertex] = self.level[u] + 1
                    queue.append(edge.to_vertex)
        return self.level[t] > 0

    def dfs(self, u, t, flow):
        if u == t:
            return flow

        additional_flow = 0
        for edge in self.adj[u]:
            if edge.capacity > edge.flow and self.level[edge.to_vertex] == self.level[u] + 1:
                d_flow_path = self.dfs(edge.to_vertex, t, min(flow, edge.capacity - edge.flow))
                if d_flow_path > 0:
                    edge.flow += d_flow_path
                    edge.reversed_edge.flow -= d_flow_path
                    additional_flow += d_flow_path
                    flow -= d_flow_path
                    if flow == 0:
                        break

        if additional_flow == 0:
            self.level[u] = -2

        return additional_flow

    def max_flow(self, s, t):
        max_flow = 0
        round = 0
        while self.bfs(s, t):
            max_flow += self.dfs(s, t, float('inf'))
            self.print(round)
            round += 1
        return max_flow

    def print(self, round):
        print("----------------round:", round)
        for (u, v, capacity) in self.debug_edge:
            for edge in self.adj[u]:
                if edge.to_vertex == v:
                    print(u+1, "to", v+1, ":", edge.flow, "/", capacity, end="   ")
            for edge in self.adj[v]:
                if edge.to_vertex == u:
                    print(" res ", edge.flow, "/", 0)


if __name__ == '__main__':
    import sys

    sys.stdin = open('input.txt', 'r')

    n, m, A, B = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)

    print(graph.max_flow(A - 1, B - 1))
