mySet = Set()
for a in 2:100
    for b in 2:100
        push!(mySet, big(a) ^ big(b))
    end    
end    
println(length(mySet))
