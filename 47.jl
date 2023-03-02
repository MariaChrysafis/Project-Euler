using Primes
for i in 1:1000000
    if length(factor(i)) == 4 && length(factor(i + 1)) == 4 && length(factor(i + 2)) == 4 && length(factor(i + 3)) == 4
        println(i)
        break
    end
end
