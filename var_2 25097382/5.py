def solution(n):
    bin_n = bin(n)[2:]
    for _ in (0, 1):
        bin_n = f'{bin_n}{sum([int(i) for i in bin_n]) % 2}'
    return int(f'0b{bin_n}', 2)


for x in range(100):
    if solution(x) > 253:
        print(x, solution(x))  # 64
