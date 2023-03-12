#include <iostream>
#include <map>
#include <vector>
#include <set>
using namespace std;


const int64_t MAX = 1e2;
const int64_t MOD = 1e9;
const int64_t sq = 1e1;
int is_prime[sq + 1];
vector<int> primes;
map<int64_t,int64_t> dp[sq + 1];
map<int64_t,int64_t> dp_sum[sq + 1];

int64_t mult (int64_t a, int64_t b) {
    return (a * b) % MOD;
}

int64_t add (int64_t a, int64_t b) {
    return (a + b) % MOD;
}

int64_t sub (int64_t a, int64_t b) {
    return (a - b + MOD) % MOD;
}

void dfs (int p, int64_t x) {
    if (dp[p].count(x)) {
        return;
    }
    if (p == 0) {
        dp[p][x] = x - x/primes[p];
        int64_t fl2 = (x/2) % MOD;
        dp_sum[p][x] = (((x % MOD) * (x % MOD + 1))/2) % MOD - (fl2 % MOD * (fl2 + 1) % MOD) + MOD;
        dp_sum[p][x] %= MOD;
    } else {
        dfs(p - 1, x);
        dfs(p - 1, x/primes[p]);
        dp[p][x] = sub(dp[p - 1][x], dp[p - 1][x/primes[p]]);
        dp_sum[p][x] = sub(dp_sum[p - 1][x], mult(dp_sum[p - 1][x/primes[p]], primes[p]));
    }
}

int main () {
    for (int i = 0; i <= sq; i++) {
        is_prime[i] = true;
    }
    is_prime[0] = false;
    is_prime[1] = false;
    vector<int> needed;
    for (int i = 2; i <= sq; i++) {
        if (is_prime[i]) {
            int j = 2 * i;
            while (j <= sq) {
                is_prime[j] = false;
                j += i;
            }
            primes.push_back(i);
        }
    }
    for (int i = 1; i <= sq; i++) {
        needed.push_back(i);
        needed.push_back(MAX/i);
    }
    cout << needed.size() << '\n';
    map<int64_t,int64_t> cur, prev, cur_sum, prev_sum;
    int64_t ans = 0;
    for (int p = 0; p < primes.size(); p++) {
        prev = cur;
        prev_sum = cur_sum;
        for (int x: needed) {
            if (p == 0) {
                cur[x] = x - x/primes[p];
                auto f1 = x;
                auto f2 = (f1/2) % MOD;
                f1 %= MOD;
                cur_sum[x] = (((f1 * (f1 + 1)) / 2) % MOD - ((f2 * (f2 + 1))) % MOD + MOD) % MOD;
            } else {
                cur[x] = sub(prev[x], prev[x / primes[p]]);
                cur_sum[x] = sub(prev_sum[x], mult(prev_sum[x / primes[p]], primes[p]));
            }
        }
        if (p != 0) {
            ans += mult(sub(prev[MAX], cur[MAX]), primes[p]);
            ans %= MOD;
        } else {
            ans += mult(cur[MAX], primes[p]);
            ans %= MOD;
        }
    }
    ans += cur_sum[MAX] - 1;
    cout << ans;

}

