#include <iostream>
#include <map>
#include <iomanip>
#include <functional>
const int MOD = 1e9 + 7;
using namespace std;
//What is our expected score if we use n moves?
int64_t gcd (int64_t a, int64_t b) {
    if (!a or !b) return max(a, b);
    return gcd(max(a, b) % min(a, b), min(a, b));
}
int64_t lcm (int64_t a, int64_t b) {
    return (a * b)/gcd(a, b);
}
int64_t binPow (int64_t x, int y) {
    int64_t ans = 1;
    int64_t res = x;
    while (y > 0) {
        if (y & 1) {
            ans *= res, ans %= MOD;
        }
        res *= res, res %= MOD;
        y /= 2;
    }
    return ans;
}
int main () {
    int n = 800;
    auto brute = [&] (int n) {
        int res = 0;
        for (int i = 0; i < (1 << n); i++) {
            int g = 1;
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    g = lcm(g, j + 1);
                }
            }
            res += g;
            //cout << g << '\n';
        }
        return res;
    };
    vector<int> primes; //set of primes <= n
    for (int i = 2; i <= n; i++) {
        bool is_prime = true;
        for (int j = 2; j <= i - 1; j++) {
            if (i % j == 0) {
                is_prime = false;
            }
        }
        if (is_prime) {
            primes.push_back(i);
        }
    }
    map<vector<int>, int64_t> myMap;
    function<int64_t(vector<int>, int)> pruned = [&] (vector<int> v, int x) {
        sort(v.begin(), v.end());
        if (myMap.count(v)) {
            return myMap[v];
        }
        //cout << v.size() << '\n';
        reverse(v.begin(), v.end());
        int64_t mult = 1;
        while (!v.empty() and v.back() == 1){
            mult *= 2;
            mult %= MOD;
            v.pop_back();
        }
        reverse(v.begin(), v.end());
        //cout << "SIZE " v.size() << '\n';
        if (v.empty()) {
            return mult;
        }
        vector<int64_t> dp;
        for (int powr = 0; pow(primes[x], powr) <= n; powr++) {
            vector<int> new_v;
            for (int i: v) {
                if (i % (int)pow(primes[x], powr + 1) == 0) {
                    continue;
                }
                while (i % primes[x] == 0) {
                    i /= primes[x];
                }
                new_v.push_back(i);
            }
            dp.push_back(pruned(new_v, x + 1));
        }
        for (int i = 1; i < dp.size(); i++) {
            //exactly powr of i
            for (int j = 0; j < i; j++) {
                dp[i] -= dp[j];
                dp[i] += MOD;
                dp[i] %= MOD;
            }
        }
        for (int i = 0; i < dp.size(); i++) {
            dp[i] *= binPow(primes[x], i) % MOD;
            dp[i] %= MOD;
        }
        int64_t sum = 0;
        for (int64_t i: dp) {
            sum += i;
            sum %= MOD;
        }
        myMap[v] = sum;
        return (sum * mult) % MOD;
    };
    vector<int> vv;
    for (int i = 1; i <= n; i++) vv.push_back(i);
    cout << pruned(vv, 0) << '\n'; //15 + 3 + 5 + 1 = 24
}
