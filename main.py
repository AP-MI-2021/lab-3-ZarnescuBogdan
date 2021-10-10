def create_lst_max(lst, init, k_max):
    '''
    Creeaza cea mai lunga subsecventa cu o anumita proprietate.
    :param init: int
    :param k_max: int
    :return: lst_max
    '''
    lst_max = []
    for i in range(init, init + k_max):
        lst_max.append(lst[i])
    return lst_max

def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca numerele sunt ordonate crescator.
    :param lst: int
    :return: lst_max
    '''
    k = 1
    k_max = -1
    for i in range(1, len(lst)):
        if(lst[i] > lst[i-1]):
            k = k+1
        else:
            if k > k_max:
                k_max = k
                init = i - k_max
            k = 1
    if len(lst) == 0:
        return lst
    else:
        if k > k_max:
            k_max = k
            init = len(lst) - k_max
        return create_lst_max(lst, init, k_max)

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([3, 4, 3, 5, 6]) == [3, 5, 6]
    assert get_longest_sorted_asc([3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]

def is_prime(x):
    '''
    Determina daca un numar este prim.
    :param x: int
    :return: True daca x este prim, respectiv False in caz contrar.
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(3) is True
    assert is_prime(1) is False
    assert is_prime(6) is False

def prime_digits(nr):
    '''
    Determina daca un numar este format doar din cifre prime.
    :param nr: int
    :return: True daca x este format doar din cifre prime, respectiv False in caz contrar.
    '''
    while nr:
        if is_prime(nr % 10) is False:
            return False
        nr = nr // 10
    return True

def test_prime_digits():
    assert prime_digits(234) is False
    assert prime_digits(235) is True

def get_longest_prime_digits(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt formate din cifre prime.
    :param lst: int
    :return: lst_max: int
    '''
    k = 0
    k_max = -1
    for i in range(len(lst)):
        nr = lst[i]
        if prime_digits(nr):
            k = k + 1
        else:
            if k > k_max:
                k_max = k
                init = i - k_max
            k = 0
    if k > k_max:
        k_max = k
        init = len(lst) - k_max
    return create_lst_max(lst, init, k_max)

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([3, 4, 3, 5, 6]) == [3, 5]
    assert get_longest_prime_digits([2, 3, 5, 7, 23]) == [2, 3, 5, 7, 23]

def print_menu():
    print('1.Citire date.')
    print('2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt ordonate crescător.')
    print('3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt formate din cifre prime.')
    print('4. Iesire')

def read_list():
    lst = []
    n = int(input('Lungimea listei: '))
    for i in range(n):
        lst.append(int(input('lst[' + str(i) + '] = ')))
    return lst

def main():
    lst = []
    while True:
        print_menu()
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            lst = read_list()
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
test_is_prime()
test_prime_digits()
if __name__ == '__main__':
    main()