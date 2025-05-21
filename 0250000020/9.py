k = 0
for s in open('9 _megatext.txt'):
    a = [int(x) for x in s.split()]
    par = [x for x in a if a.count(x) == 2]
    ne_par = [x for x in a if a.count(x) == 1]
    if len(par) == 2 and len(ne_par) == 3 and sum(par) < sum(ne_par):
        k += 1
print(k)  # 1504
