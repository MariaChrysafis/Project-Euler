using Primes

function getter(N::Int64)
    ans::Int64 = 0
    for i in 1:N
        if i * i > N
            break
        end
        ans += div(N, i)
    end
    ans *= 2
    gamma::Int64 = floor(sqrt(N))
    return ans - gamma * gamma
end


function f(N::Int64)
    mx::Int64 = floor(sqrt(N)) + 10
    phi::Array{Int} = zeros(1, mx + 10)
    for i in 1:mx
        phi[i] = i
    end
    for i in 2:mx
        if phi[i] < i
            continue
        end
        j = i
        while j <= mx
            phi[j] -= div(phi[j], i)
            j += i
        end
    end
    ans::Int64 = 0
    for f::Int64 in 1:N
        if f * f > N
            break
        end
        ans += phi[f] * getter(div(N, f * f))
    end
    return ans
end

function main()
    base::Int64 = 10
    println(f(base^15))
end
main()
