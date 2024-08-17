#include <vector>
#include <iostream>
#include <cmath>
#include <cassert>
using namespace std;
const long long MOD = (long long)987654321;
class Matrix {
public:
    Matrix operator* (const Matrix&);
    vector<vector<long long>> mat;
    Matrix (int n, int m) {
        mat.resize(n);
        for (int i = 0; i < n; i++) {
            mat[i].assign(m, 0);
        }
    }
};
std::ostream& operator << (std::ostream& stream, const Matrix& matrix) {
    for (int i = 0; i < matrix.mat.size(); i++) {
        for (int j = 0; j < matrix.mat[i].size(); j++) {
            stream << matrix.mat[i][j] << ' ';
        }
        cout << '\n';
    }
    return stream;
}
Matrix Matrix::operator* (const Matrix& m2) {
    assert(this->mat[0].size() == m2.mat.size());
    Matrix m((int)this->mat.size(), (int)m2.mat.size());
    for (int i = 0; i < this->mat.size(); i++)  {
        for (int j = 0; j < m2.mat.size(); j++) {
            for (int k = 0; k < this->mat[0].size(); k++) {
                m.mat[i][j] += (this->mat[i][k] * m2.mat[k][j]) % MOD;
                m.mat[i][j] %= MOD;
            }
        }
    }
    return m;
}
Matrix ident (int n) {
    Matrix m = Matrix(n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            m.mat[i][j] = (i == j);
        }
    }
    return m;
}
Matrix powr (const Matrix m, long long y) {
    Matrix ans = ident(m.mat.size());
    Matrix res = m;
    while (y > 0LL) {
        if (y & 1LL) {
            ans = ans * res;
        }
        res = res * res;
        y /= 2LL;
    }
    return ans;
}
long long powr (long long x, long long y) {
    long long ans = 1, res = x;
    while (y > 0) {
        if (y & 1LL) {
            ans = ans * res;
            ans %= MOD;
        }
        res = res * res;
        res %= MOD;
        y /= 2LL;
    }
    return ans;
}


int main() {
    long long n = 1e7, k = 1e12;
    int lpf[n + 1];
    for (int i = 0; i <= n; i++) {
        lpf[i] = i;
    }
    for (int i = 2; i <= n; i++) {
        if (lpf[i] == i) {
            int j = 2 * i;
            while (j <= n) {
                lpf[j] = i;
                j += i;
            }
        }
    }
    auto reduce = [&] (int x) {
        int ans = -1;
        while (x != 1) {
            ans += 1;
            x /= lpf[x];
        }
        return ans;
    };
    int mx = (int)log2(n);
    mx += 1;
    vector<int> nim = {0};
    for (int i = 0; i < 1000; i++) {
        if (__builtin_popcount(i) % 2 == 1) {
            nim.push_back(i);
        }
    }
    mx = 128;
    vector<int> cnt; cnt.assign(mx, 0);
    for (int i = 2; i <= n; i++) {
        // cout << i << " " << reduce(i) << '\n';
        cnt[nim[reduce(i)]] += 1;
    }
    Matrix m = Matrix(mx, mx);
    for (int mask1 = 0; mask1 < mx; mask1++) {
        for (int i = 0; i < cnt.size(); i++) {
            m.mat[mask1][mask1 ^ i] += cnt[i];
        }
    }
    m = powr(m, k);
    cout << (powr(n - 1, k) - m.mat[0][0] + MOD) % MOD;
}
