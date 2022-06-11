#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <tuple>
#include <set>

using namespace std;


int dijkstra(vector<vector<int>> table, int n, int t) {
    vector<vector<int>> dist(n, vector<int>(n, 0));
    vector<vector<int>> seen(n, vector<int>(n, 0));
    seen[0][0] = 1;
    priority_queue<tuple<int, int, int>> pq;
    pq.push(make_tuple(0, 0, 0));
    int i, j, di, dj, d0, i0, j0;
    while (not pq.empty()) {
        auto cur = pq.top();
        d0 = -get<0>(cur), i0 = get<1>(cur), j0 = get<2>(cur);
        pq.pop();
        if (i0 == n - 1 and j0 == n - 1)
            return d0;
        for (auto dd: {make_pair(1, 0), make_pair(-1, 0), make_pair(0, 1), make_pair(0, -1)}) {
            di = get<0>(dd), dj = get<1>(dd);
            i = i0 + di, j = j0 + dj;
            if (i < 0 or i >= n or j < 0 or j >= n or seen[i][j]) continue;
            seen[i][j] = 1;
            pq.push(make_tuple(-(d0 + table[i][j]), i, j));
            dist[i][j] = d0 + table[i][j];
        }
    }
    return -1;
}
