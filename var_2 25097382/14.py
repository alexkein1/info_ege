res = []
for x in range(1, 2301):
    s = 7 ** 350 + 7 ** 150 - x
    k = ''
    while s != 0:
        k = str(s % 7) + k
        s //= 7
    if k.count('0') == 200:
        res.append(x)
print(res)  # 2001
