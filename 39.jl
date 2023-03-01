using Primes
function f(n::Integer)
    dict::Dict{Integer, Integer} = Dict()
    for a = 1:n, b = 1:n
        c::Integer = a * a + b * b
        if floor(sqrt(c)) * floor(sqrt(c)) == c
            c = floor(sqrt(c))
            if a + b + c > n
                continue
            end
            if haskey(dict, a + b + c)
                dict[a + b + c] = dict[a + b + c] + 1
            else
                dict[a + b + c] = 1
            end
            println(a + b + c)
        end
    end
    ind = 0
    myMax = 0
    for (val, key) in dict
        if key > myMax
            ind = val
            myMax = key
        end
    end
    return ind
end
println(f(1000))
