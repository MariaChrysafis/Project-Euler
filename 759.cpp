#include <iostream>
#include <map>
using namespace std;

map<pair<int64_t,int>,int> dict, dict1, dict2;
int mod = 1e9 + 7;

int64_t binPow (int64_t x, int y) {
    int64_t res = x, ans = 1;
    while (y > 0) {
        if (y & 1) {
            ans *= res;
            ans %= mod;
        }
        res *= res, res %= mod, y /= 2;
    }
    return ans;
}

int64_t getlog (int64_t n) {
    int left = 0;
    int right = 63;
    while (left != right) {
        int mid = (left + right + 1)/2;
        if ((int64_t(1) << mid) <= n) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
}

int64_t count(int64_t n, int k) {
    if (k == 0 || n == 0) {
        return 0;
    }
    if (dict.count(make_pair(n, k))) {
        return dict[make_pair(n, k)];
    }
    int lg2 = getlog(n);
    if (k == 1) {
        return lg2 + 1;
    }
    int64_t ans = 0;
    for (int i = 1; i <= lg2 - 1; i++) {
        ans += count(((int64_t)1 << i) - 1, k - 1);
        ans %= mod;
    }
    ans += count(n - ((int64_t)1 << lg2), k - 1);
    ans %= mod;
    return dict[make_pair(n, k)] = ans;
}

int64_t countx(int64_t n, int k) {
    if (k == 0 || n == 0) {
        return 0;
    }
    if (dict1.count(make_pair(n, k))) {
        return dict1[make_pair(n, k)];
    }
    int lg2 = getlog(n);
    if (k == 1) {
        return binPow(2, lg2 + 1) - 1;
    }
    int64_t ans = 0;
    for (int i = 1; i <= lg2 - 1; i++) {
        ans += countx(((int64_t)1 << i) - 1, k - 1) + (count(((int64_t)1 << i) - 1, k - 1) * binPow(2, i)) % mod;
        ans %= mod;
    }
    ans += countx(n - ((int64_t)1 << lg2), k - 1) + (count(n - ((int64_t)1 << lg2), k - 1) * binPow(2, lg2)) % mod;
    ans %= mod;
    return dict1[make_pair(n, k)] = ans;
}

int64_t countxx(int64_t n, int k) {
    if (k == 0 || n == 0) {
        return 0;
    }
    if (dict2.count(make_pair(n, k))) {
        return dict2[make_pair(n, k)];
    }
    int lg2 = getlog(n);
    if (k == 1) {
        int64_t ans = 0;
        for (int i = 0; i <= lg2; i++) {
            ans += binPow(2, 2 * i);
        }
        return ans;
    }
    int64_t ans = 0;
    for (int i = 1; i <= lg2 - 1; i++) {
        ans += (binPow(2, 2 * i) * count(((int64_t)1 << i) - 1, k - 1)) % mod + (binPow(2, i + 1) * countx(((int64_t)1 << i) - 1, k - 1)) % mod + countxx(((int64_t)1 << i) - 1, k - 1);
        ans %= mod;
    }
    ans += (binPow(2, 2 * lg2) * count(n - ((int64_t)1 << lg2), k - 1)) % mod + (binPow(2, lg2 + 1) * countx(n - ((int64_t)1 << lg2), k - 1)) % mod + countxx(n - ((int64_t)1 << lg2), k - 1);
    ans %= mod;
    return dict2[make_pair(n, k)] = ans;
}

int main() {
    int64_t ans = 0;
    int64_t N = 1e16;
    for (int i = 1; i <= 63; i++) {
        ans += (countxx(N, i) * i * i) % mod;
        ans %= mod;
    }
    cout << ans;
}
