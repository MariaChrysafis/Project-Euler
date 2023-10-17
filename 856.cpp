#include <iostream>
#include <map>
#include <iomanip>
using namespace std;
map<pair<vector<int>, int>, double> dp;
double dfs (vector<int> v, int x) { //last card
    int vx = v[x];
    auto undo = [&] () {
        sort(v.begin(), v.end());
        for (int i = 0; i < v.size(); i++) {
            if (v[i] == vx) {
                x = i;
                break;
            }
        }
    };
    undo();
    int sum = 0;
    for (int i: v) {
        sum += i;
    }
    if (dp.count(make_pair(v, x))) {
        return dp[make_pair(v, x)];
    }
    if (sum == 0) {
        return sum;
    }
    //if we choose v[x]
    double ans = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] == 0) continue;
        if (i == x) {
            ans += (double)v[i]/(double)sum;
        } else {
            v[i] -= 1;
            ans += ((double)v[i] + 1)/(double)sum * (dfs(v, i) + 1);
            v[i] += 1;
        }
    }
    return (dp[make_pair(v, x)] = ans);
}
int main () {
    vector<int> v;
    v.assign(13, 4);
    cout << setprecision(30) << dfs(v, -1) << '\n';
}

