import std.stdio;
void main() {
    int cur = 1;
    int prev = 1;
    int ans = 0;
    while (cur < 4000000) {
        if (cur % 2 == 0) {
            ans += cur;
        }
        cur = prev + cur;
        prev = cur - prev;
    }
    writeln(ans);
}
