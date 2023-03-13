#include <iostream>
#include <map>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>
#include <unordered_map>
using namespace std;
const int M = 998244353;
const int64_t MAX = 1e11;
vector<int64_t> get_set (int64_t x) {
    vector<int64_t> vec;
    for (int64_t i = 1; i <= x; i++) {
        if (i * i > x) {
            break;
        }
        vec.push_back(i);
        if (i != x/i) {
            vec.push_back(x/i);
        }
    }
    return vec;
}

int64_t s[(int)1e6 + 1];

int64_t get (int64_t x) {
    if (x <= 316227) {
        return x;
    }
    return MAX/x + 1 + 500000;
}

int64_t rec (int64_t x) {
    if (s[get(x)] != -1) {
        return s[get(x)];
    }
    int64_t ans = x % M * (x % M + 1)/2;
    ans %= M;
    for (auto& i: get_set(x)) {
        if (i == x) {
            continue;
        }
        ans -= (rec(i) * ((x/i) % M - (x/(i + 1)) % M + M) % M) % M;
        ans += M, ans %= M;
    }
    assert(ans >= 0 && ans < M);
    s[get(x)] = ans;
    return ans;
}


int64_t res (int64_t x) {
    int64_t ans = 0;
    for (auto& i: get_set(x)) {
        int64_t left = x/(i + 1);
        int64_t right = x/i;
        left %= M, right %= M;
        ans += (rec(i) * (((right * (right + 1))/2 % M) - ((left * (left + 1))/2) % M + M) % M) % M;
        ans %= M;
    }
    return ans;
}

int main () {
    for (int i = 0; i <= (int)1e6; i++) {
        s[i] = -1;
    }
    cout << res(MAX);
}
