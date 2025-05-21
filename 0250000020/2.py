print('x y z w  | f == 0')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not (w and ((z or y) is (z and x))):
                    if w:
                        print(f'{x} {y} {z} {w}')
