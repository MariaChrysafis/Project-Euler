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
const int mx = 150 * (int)1e6;
bool is_prime[mx];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (int i = 0; i < mx; i++) {
         is_prime[i] = true;
    }
    vector<int> primes;
    for (int i = 2; i < mx; i++) {
        if (is_prime[i]) {
            for (int j = 2 * i; j < mx; j += i) {
                is_prime[j] = false;
            }
            primes.push_back(i);
        }
    }
	//cout << primes.size() << endl;
	//exit(0);
    ll offset[] = {1, 3, 7, 9, 13, 27};
    vector<ll> pos;
    for (ll n = 10; n <= mx; n++) {
        bool fine = true;
        for (ll p: primes) {
            for (ll x: offset) {
                if ((n * n + x) % p == 0 and p != n * n + x) {
                    fine = false;
                    break;
                }
            }
            if (!fine) {
                break;
            }
        }
        if (!fine) {
        	continue;
        }
        //pos.push_back(n);
        for (int x = 1; x < 27; x += 2) {
        	if (x == 1 or x == 3 or x == 9 or x == 7 or x == 27 or x == 13) continue;
        	bool found = false;
        	for (int p: primes) {
        		if ((n * n + x) % p == 0 and p != n * n + x) {
        			found = true;
        			break;
        		}
        	}
        	if (!found) {
        		fine = false;
        		break;
        	}
        }
        if (!fine) {
        	//pos.push_back(n);
        	continue;
        }
        pos.push_back(n);
    }
    cout << "SIZE :" << pos.size() << endl;
    ll sum = 0;
    for (ll x: pos) {
    	cout << x << " ";
        sum += x;
    }
    cout << endl;
    cout << "SUM " << sum;
    exit(0);
    for (int i: pos) {
        cout << i << ' ';
    }
    cout << endl;
}
//n^2 + 3 must be n^2^(1/3)
