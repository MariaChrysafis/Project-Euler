cnt 1 = 0
cnt n = if n `mod` 3 == 0 || n `mod` 5 == 0 then cnt(n - 1) + n else cnt(n - 1)
main = do
    print(cnt 999)
    
