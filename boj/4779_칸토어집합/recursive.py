def recursive(k):
    if k == 0:
        return "-"

    return recursive(k - 1) + (" " * (3 ** (k - 1))) + recursive(k - 1)


while True:
    try:
        print(recursive(int(input())))
    except:
        break
