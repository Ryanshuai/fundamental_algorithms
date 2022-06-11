#include <iostream>
#include <vector>
#include <string>
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <tuple>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <functional>
#include <numeric>
#include <stack>

using namespace std;


class StackFind {
public:
    stack<int> s;
    vector<int> is_in_stack;

    StackFind(int n) { is_in_stack.resize(n, 0); }

    int is_in(int x) { return is_in_stack[x]; }

    void push(int x) {
        s.push(x);
        is_in_stack[x] = 1;
    }

    void pop() {
        int x = s.top();
        s.pop();
        is_in_stack[x] = 0;
    }

    int top() { return s.top(); }
};


int dfs(vector<vector<int>> &adj, vector<int> &dfn, vector<int> &low, StackFind &stack, int &order, int at, int &scc_n,
        vector<int> &scc) {
    if (dfn[at] != -1 and stack.is_in(at)) { return low[at]; }
    if (dfn[at] != -1) return adj.size();

    dfn[at] = low[at] = order++;
    stack.push(at);
    for (int to: adj[at]) {
        low[at] = min(low[at], dfs(adj, dfn, low, stack, order, to, scc_n, scc));
    }

    if (dfn[at] == low[at]) {
        while (stack.top() != at) {
            int x = stack.top();
            stack.pop();
            scc[x] = scc_n;
        }
        stack.pop();
        scc[at] = scc_n;
        scc_n++;
    }
    return low[at];
}


void targan(vector<vector<int>> &adj) {
    int n = adj.size();
    int order = 0;
    int scc_n = 0;
    vector<int> dfn(n, -1);
    vector<int> low(n, -1);
    vector<int> scc(n, -1);
    StackFind sf(n);

    for (int i = 0; i < n; i++) {
        if (dfn[i] == -1) {
            dfs(adj, dfn, low, sf, order, i, scc_n, scc);
        }
    }
    cout << endl;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    // freopen("input.txt", "r", stdin);
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a = a - 1;
        b = b - 1;
        adj[a].push_back(b);
    }

    targan(adj);

    return 0;
}