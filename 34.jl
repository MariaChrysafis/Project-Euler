function f()
  ans = 0
  for i in 3:10000000
    res = i
    for c in digits(i)
      res -= factorial(c)  
    end  
    if res == 0
      ans += i
    end  
  end  
  println(ans)
end  

f()
