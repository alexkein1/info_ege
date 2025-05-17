def main(s):
    for x in range(1000):
        if not (((x & 52 != 0) and (x & 48 == 0)) <= (not (x & s == 0))):
            return False
    return True


for a in range(1000):
    if main(a):
        print(a)  # 4
