using Primes

function f(N::Int)
    dict = Dict()
    for i::Int64 in 1:N
        s = join(sort(collect(string(i * i * i))))
        if haskey(dict, s)
            dict[s] += 1
        else
            dict[s] = 1
        end
    end
    val = []
    for (key, value) in dict
        if value == 5
            push!(val, key)
        end
    end
    ans = minimum(val)
    for i::Int64 in 1:N
        if join(sort(collect(string(i * i * i)))) == ans
            println(i * i * i)
            return
        end
    end
end
f(10000)
