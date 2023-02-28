using Primes
function f(n)
    ans = []
    for i in 1:n
        if isprime(i)
            push!(ans, i)
        end
    end
    pos = Dict()
    for i in 1:n
        if isprime(i)
            arr = []
             for j in (i + 1):n
                gamma1 = string(i) * string(j)
                gamma2 = string(j) * string(i)
                if isprime(j) && isprime(parse(Int64, gamma1)) && isprime(parse(Int64, gamma2))
                    push!(arr, j)
                end
             end
             pos[i] = arr
        end
    end
    for a in 1:n
        if !isprime(a)
            continue
        end
        for b in pos[a]
            ab = intersect!(pos[b], pos[a])
            for c in ab
                abc = intersect!(ab, pos[c])
                for d in abc
                    for e in intersect!(abc, pos[d])
                        println([a, b, c, d, e])
                    end
                end
            end
        end
    end
end
println(f(20000))
