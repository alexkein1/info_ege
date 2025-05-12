print(f'x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not ((x and not y) or (y is z) or w):
                    print(f'{x} {y} {z} {w}')

# x y z w
# 0 0 1 0
# 0 1 0 0
# 1 1 0 0

# xwzy
