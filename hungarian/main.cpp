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


using namespace std;


bool find(int i, vector<vector<int>> &is_connected, vector<int> &assign_to, vector<int> &tried) {
    int n = is_connected.size();
    for (int j = 0; j < n; j++) {
        if (is_connected[i][j] && tried[j] == 0) {
            tried[j] = 1;
            if (assign_to[j] == -1 or find(assign_to[j], is_connected, assign_to, tried)) {
                assign_to[j] = i;
                return true;
            }
        }
    }
    return false;
}


int hungarian(vector<vector<int>> &is_connected) {
    int n = is_connected.size();
    vector<int> assign_to(n, -1);
    vector<int> tried(n, 0);
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) tried[j] = 0;
        if (find(i, is_connected, assign_to, tried)) count++;
    }
    return count;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("input.txt", "r", stdin);

    int T;
    cin >> T;

    int n;


    for (int t = 0; t < T; t++) {
        cin >> n;
        vector<vector<int>> mat;
        for (int i = 0; i < n; i++) {
            vector<int> row;
            for (int j = 0; j < n; j++) {
                int x;
                cin >> x;
                row.push_back(x);
            }
            mat.push_back(row);
        }
        if (hungarian(mat) == n) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
