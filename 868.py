def rec(input: list[chr]) -> int:
    if len(input) == 1 :
        return 0
    ind = 25
    while ind >= 0:
        c = chr(ord('A') + ind)
        if c in str(input):
            orig = input.copy()
            ind = input.index(c)
            input.remove(c)
            new_s = input.copy()
            ans = rec(new_s.copy())
            if ans % 2 == 0:
                return ans * len(orig) + len(input) - ind
            else:
                return ans * len(orig) + ind
        ind = ind - 1
my_string = "NOWPICKBELFRYMATHS"
print(rec(list(my_string)))
