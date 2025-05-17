k = 0
res = []
a = [int(i) for i in open('17_21903.txt')]
possible_funny_number = []
for n in a:
    if str(n).endswith('15') and len(str(n)) == 3:
        possible_funny_number.append(n)
funny_number = min(possible_funny_number)
for x in range(len(a) - 2):
    t = [a[x], a[x + 1], a[x + 2]]
    if not all((t[0] < 0, t[1] < 0, t[2] < 0)) and not all((t[0] >= 0, t[1] >= 0, t[2] >= 0)):
        continue
    proiz = min(t) * max(t)
    if proiz > funny_number ** 2:
        k += 1
        res.append(proiz)
print(k, min(res))
