mx = 5000
issquare = set()
for i in range(0, mx) :
    issquare.add(i * i)
adj = []
for i in range(0, mx + 1) :
    adj.append(set())
for a1 in range(0, mx + 1) :
    for b1 in range(a1 + 1, mx + 1) :
        if b1 * b1 - a1 * a1 in issquare :
            adj[a1].add(b1)
ans = pow(10, 10)
for a1 in range(1, mx + 1) :
    for b1 in adj[a1] :
        set_c = adj[a1].intersection(adj[b1]) 
        for c1 in set_c :
            assert c1 > a1 and c1 > b1
            d = a1 * a1 + b1 * b1 + c1 * c1
            if (a1 + b1 + c1) % 2 == 0 and a1 + b1 + c1 < ans:
                a = a1 * a1
                b = b1 * b1
                c = c1 * c1
                my_sum = (a1 * a1 + b1 * b1 + c1 * c1)//2
                x = my_sum - a
                y = my_sum - b
                z = my_sum - c
                if x > 0 and y > 0 and z > 0 :
                    ans = min(ans, a1 * a1 + b1 * b1 + c1 * c1)
                    print(x, y, z)
print(ans//2)

