def f(s, m):
    if s >= 67:
        return m % 2 == 0
    if m == 0:
        return 0
    move = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
    return any(move) if m % 2 == 1 else all(move)


print(f'19: {[s for s in range(1, 67) if f(s, 2) and not f(s, 1)]}')  # 22
print(f'20: {[s for s in range(1, 67) if f(s, 3) and not f(s, 1)]}')  # 18, 21
print(f'21: {[s for s in range(1, 67) if f(s, 4) and not f(s, 2)]}')  # 17
