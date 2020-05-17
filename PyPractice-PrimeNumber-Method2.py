from math import sqrt


def main():
    s = []
    for i in range(100, 999):
        k = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                k = False
                break
        if k:
            s.append(i)
    print(s)


if __name__ == '__main__':
    main()
