using Primes
for i in 1:10000000
    x = sort(digits(i))
    x2 = sort(digits(2 * i))
    x3 = sort(digits(3 * i))
    x4 = sort(digits(4 * i))
    x5 = sort(digits(5 * i))
    x6 = sort(digits(6 * i))
    if x == x2 && x == x3 && x == x4 && x == x5 && x == x6
         println(i)
    end
end
