#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <functional>
#define ll long long
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    const int mx = 150 * (int)1e6; //3 * 10^5 of such numbers
    const int mx_prime = mx;
    bool is_prime[mx_prime];
    for (int i = 0; i < mx_prime; i++) {
         is_prime[i] = true;
    }
    vector<int> primes;
    //int cntr = 0;
    for (int i = 2; i < mx_prime; i++) {
        if (is_prime[i]) {
            for (int j = 2 * i; j < mx_prime; j += i) {
                is_prime[j] = false;
            }
            //cntr++;
            primes.push_back(i);
        }
    }
    //cout << cntr;
    exit(0);
    vector<int> offset = {1, 3, 7, 9, 13, 27}; //n^2 + 11 must be composite
    vector<int> pos;
    for (ll n = 10; n <= mx; n++) {
        bool fine = true;
        for (ll p: primes) {
            for (ll x: offset) {
                if ((n * n + x) % p == 0) {
                    fine = false;
                    break;
                }
            }
            if (!fine) {
                break;
            }
        }
        if (fine) {
            pos.push_back(n);
        }
    }
    cout << pos.size() << endl;
    exit(0);
    for (int i: pos) {
        cout << i << ' ';
    }
    cout << endl;
}
