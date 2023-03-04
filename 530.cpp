#include <iostream>
#include <cmath>
#include <vector>
#include <cassert>
using namespace std;

class totient_calculator {
public:
    explicit totient_calculator(int max) : totient_(max + 1) {
        for (int i = 1; i <= max; ++i)
            totient_[i] = i;
        for (int i = 2; i <= max; ++i) {
            if (totient_[i] < i)
                continue;
            for (int j = i; j <= max; j += i)
                totient_[j] -= totient_[j] / i;
        }
    }
    int totient(int n) const {
        assert (n >= 1 && n < totient_.size());
        return totient_[n];
    }
    bool is_prime(int n) const {
        return totient(n) == n - 1;
    }
private:
    std::vector<int> totient_;
};

int count_primes(const totient_calculator& tc, int min, int max) {
    int count = 0;
    for (int i = min; i <= max; ++i) {
        if (tc.is_prime(i))
            ++count;
    }
    return count;
}

int64_t getter (int64_t N) {
    int64_t ans = 0;
    for (int64_t i = 1; i * i <= N; i++) {
        ans += N/i;
    }
    ans *= 2;
    int64_t gamma = floor(sqrt(N));
    return ans - gamma * gamma;
}
int64_t f(int64_t N) {
    auto tc = totient_calculator((int)sqrt(N));
    cout << "DONE\n";
    int64_t ans = 0;
    for (int64_t f = 1; f * f <= N; f++) {
        ans += tc.totient(f) * getter(N/(f * f));
    }
    return ans;
}
int main() {
    int64_t gamma = 1e15;
    cout << gamma << '\n';
    cout << f(gamma);
}
