import itertools


def sc(digits):
    for i in range(3):
        a, b = int(digits[i]), int(digits[i + 1])
        if a % 2 == b % 2:
            return False
    return True


k = 0
for x in itertools.product('0123456789', repeat=4):
    if len(set(x)) == 4 and sc(x):
        k += 1

print(k)  # 800
