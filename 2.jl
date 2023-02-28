function f(n)
    cur = 1
    prev = 1
    ans = 0
    while true
         if cur > n
             break
         end
         nxt = cur + prev
         prev = cur
         cur = nxt
         if cur % 2 == 0
             ans += cur
         end
    end
    ans
end
println(f(4000000))
