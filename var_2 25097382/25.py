import pprint


def podelilovo(n):
    r = 0
    for i in range(1, int(n ** 0.5) - 1):
        if n % i == 0:
            r += (n // i) + i
    return r


res = dict()
for x in range(500000, 501000):
    m = podelilovo(x)
    if str(m).endswith('6'):
        res.update({x: m})
pprint.pprint(res)
