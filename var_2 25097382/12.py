for x in range(4, 10000):
    print(x)
    s = '1' + '9' * x
    while '19' in s or '399' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '399' in s:
            s = s.replace('399', '91', 1)
        if '999' in s:
            s = s.replace('999', '3', 1)
    summary = sum([int(i) for i in s])
    if summary == 33:
        print(f'\n{x}\n{s}')  # 46
        break

