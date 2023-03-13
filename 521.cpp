#include <iostream>
#include <map>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>
#include <unordered_map>
using namespace std;
const int M = 1e9;
struct modint {
    modint() : n(0) {}
    template <class T> modint(T n) { n %= M; if (n < 0) n += M; this->n = n; }

    modint & operator+=(const modint &r) { n += r.n; if (n >= M) n -= M; return *this; }
    modint & operator-=(const modint &r) { n -= r.n; if (n < 0) n += M; return *this; }
    modint & operator*=(const modint &r) { n = (int) ((long long) n * r.n % M); return *this; }

    modint & operator--() { if (--n == -1) n = M - 1; return *this; }
    modint & operator++() { if (++n == M) n = 0; return *this; }
    modint operator--(int) { modint t = *this; --*this; return t; }
    modint operator++(int) { modint t = *this; ++*this; return t; }

    modint operator-() const { return 0 - *this; }
    modint operator+() const { return *this; }

    modint pow(long long k = M - 2) const {
        modint f = *this, p = 1;
        while (k > 0) {
            if (k % 2 == 1) f *= p;
            p *= p, k /= 2;
        }
        return f;
    }

    int mod() const { return M; }

    friend modint operator+(modint l, const modint &r) { return l += r; }
    friend modint operator-(modint l, const modint &r) { return l -= r; }
    friend modint operator*(modint l, const modint &r) { return l *= r; }

    friend bool operator==(const modint &l, const modint &r) { return l.n == r.n; }
    friend bool operator!=(const modint &l, const modint &r) { return l.n != r.n; }

    friend ostream & operator<<(ostream &out, const modint &r) { return out << r.n; }

    int n;
};

const int64_t MAX = 1e12;
const int64_t sq = 1e6;
int is_prime[sq + 1];

vector<int64_t> primes;

int64_t get (int64_t x) {
    if (x <= sq) return x;
    return MAX/x + sq;
}

int main () {
    for (int i = 0; i <= sq; i++) {
        is_prime[i] = true;
    }
    is_prime[0] = false;
    is_prime[1] = false;
    deque<int64_t> needed;
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
    sort(needed.begin(), needed.end());
    reverse(needed.begin(), needed.end());
    vector<modint> cur(needed.size() + 10), cur_sum(needed.size() + 10);
    modint ans = 0;
    modint pref = 0;
    for (int p = 0; p < primes.size(); p++) {
        auto pv = cur[get(MAX)];
        pref += primes[p];
        cur[0] = p - 1;
        cur_sum[0] = (pref - primes[p]);
        while (p != 0 && !needed.empty() && needed.back()/primes[p] < primes[p - 1]) {
            needed.pop_back();
        }
        for (auto& x: needed) {
            if (p == 0) {
                int64_t g1 = (x - x/primes[p]) % M;
                int64_t g2 = ((x + 1)/2) % M;
                cur[get(x)] = g1 + p;
                cur_sum[get(x)] = g2 * g2 + pref;
            } else {
                cur[get(x)] -= cur[get(x / primes[p])] - p;
                cur_sum[get(x)] -= pref - primes[p] + (cur_sum[get(x / primes[p])] - pref + primes[p]) * primes[p];
                cur_sum[get(x)] += pref;
            }
        }
        if (p != 0) {
            ans += ((pv - (p - 1)) - (cur[get(MAX)] - p)) * primes[p];
        } else {
            ans += (MAX - (cur[get(MAX)] - p)) * primes[p];
        }
    }
    cout << ans << '\n';
    ans += cur_sum[get(MAX)] - pref - 1;
    cout << ans;
}
