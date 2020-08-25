def sas(a):
    exist= set()

    while a != 1:
        sum = 0
        while a > 0:
            tmp = a%10
            a = a//10
            sum += tmp*tmp
        if sum in exist:
            return False
        else:
            exist.add(sum)
        a = sum
    return True

if __name__ == "__main__":
    s = 19
    k = sas(s)

    print(k)