function main()
    arr = []
    for i in 1:20
        gamma = split(readline(), " ")
        a = []
        for x in gamma
            push!(a, parse(Int, x))
        end    
        push!(arr, a)
    end
    println(arr)
    ans = 0
    for i in 1:20
        for j in 1:20
            for dx in -1:1
                for dy in -1:1
                    if dx == 0 && dy == 0
                        continue
                    end    
                    if i + 3 * dx > 20 || j + 3 * dy > 20 || i + 3 * dx <= 0 || j + 3 * dy <= 0
                        continue
                    end  
                    ans = max(ans, arr[i][j] * arr[i + dx][j + dy] * arr[i + 2 * dx][j + 2 * dy] * arr[i + 3 * dx][j + 3 * dy])
                end    
            end    
        end    
    end   
    println(ans)
end
main()
