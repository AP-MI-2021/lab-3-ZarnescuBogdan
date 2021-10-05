def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca numerele sunt ordonate crescator.
    :param lst: int
    :return: lstMax
    '''
    k = 1
    kMax = -1
    for i in range(1, len(lst)):
        if(lst[i] > lst[i-1]):
            k = k+1
        else:
            if k > kMax:
                kMax = k
                init = i - kMax
            k = 1
    if(k > kMax):
        kMax = k
        init = len(lst) - kMax
    lstMax = []
    for i in range(init, init + kMax):
        lstMax.append(lst[i])
    return lstMax
def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([3, 4, 3, 5, 6]) == [3, 5, 6]
    assert get_longest_sorted_asc([3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]

def get_longest_prime_digits(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt formate din cifre prime.
    :param lst: int
    :return: lstMax: int
    '''
    k = 0
    kMax = -1
    for i in range(0, len(lst)):
        x = lst[i]
        while x:
            ok = 1
            if x % 10 == 1 or x % 10 == 4 or x % 10 == 6 or x % 10 == 8 or x % 10 == 9:
                ok = 0
                break
            x = x // 10
        if ok == 1:
            k = k + 1
        else:
            if k > kMax:
                kMax = k
                init = i - kMax
            k = 0
    if k > kMax:
        kMax = k
        init = len(lst) - kMax
    lstMax = []
    for i in range(init, init + kMax):
        lstMax.append(lst[i])
    return lstMax
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([3, 4, 3, 5, 6]) == [3, 5]
    assert get_longest_prime_digits([2, 3, 5, 7, 23]) == [2, 3, 5, 7, 23]

def main():
    while True:
        print('1.Citire date.')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt ordonate crescător.')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt formate din cifre prime.')
        print('4. Iesire')
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            lst = []
            n = int(input('Lungimea listei: '))
            for i in range(0, n):
                x = int(input())
                lst.append(x)
        elif optiune == '2':
            print(get_longest_sorted_asc(lst))
        elif optiune == '3':
            print(get_longest_prime_digits(lst))
        elif optiune == '4':
            break
        else:
            print('Optiune invalida.')

test_get_longest_sorted_asc()
test_get_longest_prime_digits()
main()