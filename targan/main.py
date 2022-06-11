class StackFind:
    def __init__(self, n):
        self.stack = []
        self.in_stack = [False] * n

    def is_in(self, x):
        return self.in_stack[x]

    def push(self, x):
        if not self.in_stack[x]:
            self.stack.append(x)
            self.in_stack[x] = True

    def pop(self):
        if self.stack:
            x = self.stack.pop()
            self.in_stack[x] = False
            return x
        else:
            return -1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


def dfs(adj, dfn, low, stack, order, at, scc_n, scc):
    if dfn[at] != -1 and stack.is_in(at):
        return low[at]
    if dfn[at] != -1:
        return len(adj)

    dfn[at] = low[at] = order
    order += 1
    stack.push(at)
    for to in adj[at]:
        low[at] = min(low[at], dfs(adj, dfn, low, stack, order, to, scc_n, scc))

    if dfn[at] == low[at]:
        while (stack.top() != at):
            x = stack.pop()
            scc[x] = scc_n
        stack.pop()
        scc[at] = scc_n
        scc_n += 1
    return low[at]


def targan(adj):
    n = len(adj)
    order = 0
    scc_n = 0
    dfn = [-1] * n
    low = [-1] * n
    scc = [-1] * n
    stack = StackFind(n)
    for i in range(n):
        if dfn[i] == -1:
            dfs(adj, dfn, low, stack, order, i, scc_n, scc)
    return scc


if __name__ == '__main__':
    import sys

    sys.stdin = open("input.txt", "r")

    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)

    scc = targan(adj)
    print(scc)
