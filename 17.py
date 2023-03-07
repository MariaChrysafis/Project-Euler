import inflect
p = inflect.engine()
ans = 0
for i in range(1, 1001) :
    s = p.number_to_words(i)
    s = s.replace(' ', '')
    s = s.replace(',', '')
    s = s.replace('-', '')
    ans += len(s)
print(ans)
