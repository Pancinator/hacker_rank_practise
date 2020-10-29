def saveThePrisoner(n, m, s):
    resultField = []
    candies = m

    for i in range(s, n + 1):
        if candies > 0:
            resultField.append(i)
            candies -= 1
        else:
            return resultField[len(resultField) -1]
    while True:
        for j in range(1, n + 1):
            if candies > 0:
                resultField.append(j)
                candies -= 1
            else:
                return resultField[len(resultField)-1]

def saveThePrisoners2(n, m, s):
    res1 = n - (s - 1)
    res2 = m - res1
    res3 = res2 % n
    if (res3 == 0):
        res3 = n
    return res3
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])
        result = saveThePrisoners2(n, m, s)
        print(result)


