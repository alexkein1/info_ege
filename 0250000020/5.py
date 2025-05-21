def func(n):
    n_bin = bin(n)[2:]
    if n % 2 != 0:
        new_n_bin = ''
        for num in n_bin:
            if int(num) == 0:
                new_n_bin += '1'
            elif int(num) == 1:
                new_n_bin += '0'
        n_bin = new_n_bin
    bin_r = ''
    for x in n_bin:
        if int(x) == 0:
            bin_r += '00'
        elif int(x) == 1:
            bin_r += '11'
    r = bin_r
    return int(f'0b{r}', 2)


print(func(6))
print(func(5))
for nn in range(1, 100):
    if func(nn) > 60:
        print(nn)  # 8
        break
