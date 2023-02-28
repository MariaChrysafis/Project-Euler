function f(n)
    ans = 0
    for i in 1:n - 1
        if i % 3 == 0 || i % 5 == 0
             ans += i
        end
    end
    ans
end
println(f(1000))
