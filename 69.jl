using Primes

function f(N::Int)
    arr = []
    for n in 1:N
        push!(arr, [n, totient(n)])
    end
    ind = 1
    for i in 1:length(arr)
        if arr[i][1] * arr[ind][2] > arr[ind][1] * arr[i][2]
            ind = i
        end
    end
    println(ind)
end

f(1000000)
