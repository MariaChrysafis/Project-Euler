using Primes
function nxt(n)
    return ((n % 2 == 0) ? n/2 : 3 * n + 1);
end
function f(n)
    dict = Dict()
    dict[1] = 0
    for i in 2:n
        cur = i
        length = 0
        while !haskey(dict, cur)
            cur = nxt(cur)
            length += 1
        end
        dict[i] = length + dict[cur]
    end
    ind = 0
    myMax = -1
    for (key, value) in dict
        if myMax < value
            myMax = value
            ind = key
        end
    end
    println(ind)
end
f(1000000)
