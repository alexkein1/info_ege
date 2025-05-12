k = 0
for s in open('9_source.txt'):
    a = [int(x) for x in s.split()]
    a.sort()
    if len(set(a)) == 5 and a[4] + a[3] <= sum((a[0], a[1], a[2])):
        k += 1
print(k)  # 1922
