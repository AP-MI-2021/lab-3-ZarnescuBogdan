def all_sorted_asc(lst):
    '''
    Determina daca toate numerele dintr-o lista sun ordonate crescator.
    :param lst: list[int]
    :return: True, daca toate nr. din lst sunt ordonate crescator sau False, in caz contrar
    '''
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    return True

def test_all_sorted_asc():
    assert all_sorted_asc([2, 3, 4]) is True
    assert all_sorted_asc([2, 4, 3]) is False
    assert all_sorted_asc([]) is True

def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca numerele sunt ordonate crescator.
    :param lst: list[int]
    :return: subsecventa_max: list[int]
    '''
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_sorted_asc(lst[i:j+1]) is True and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([3, 4, 3, 5, 6]) == [3, 5, 6]
    assert get_longest_sorted_asc([3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]
    assert get_longest_sorted_asc([]) == []

def all_prime_digits(lst):
    '''
    Determina daca toate numerele dintr-o lista sunt formate din cifre prime.
    :param lst: list[int]
    :return: True, daca toate nr. din lst sunt formate din cifre prime sau False, in caz contrar
    '''
    for x in lst:
        if prime_digits(x) is False:
            return False
    return True

def test_all_prime_digits():
    assert all_prime_digits([2, 3, 4]) is False
    assert all_prime_digits([2, 5, 3]) is True
    assert all_prime_digits([]) is True

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
    :param lst: list[int]
    :return: subsecventa_max: list[int]
    '''
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_prime_digits(lst[i:j+1]) is True and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([3, 4, 3, 5, 6]) == [3, 5]
    assert get_longest_prime_digits([2, 3, 5, 7, 23]) == [2, 3, 5, 7, 23]

def sum(lst):
    '''
    Determina suma numerelor dintr-o lista.
    :param lst: list[int]
    :return:
    '''
    suma = 0
    for x in lst:
        suma = suma + x
    return suma

def test_sum():
    assert sum([2, 3, 4]) == 9
    assert sum([3, 5, 0]) == 8
    assert sum([]) == 0

def get_longest_sum_is_prime(lst):
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt formate din cifre prime.
    :param lst: list[int]
    :return: subsecventa_max: list[int]
    '''
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if is_prime(sum(lst[i:j+1])) is True and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([3, 5, 7, 8]) == [3, 5, 7, 8]
    assert get_longest_sum_is_prime([]) == []
    assert get_longest_sum_is_prime([3, 5, 7, 1]) == [5, 7, 1]

def test_all():
    test_all_sorted_asc()
    test_get_longest_sorted_asc()
    test_all_prime_digits()
    test_is_prime()
    test_prime_digits()
    test_get_longest_prime_digits()
    test_sum()
    test_get_longest_sum_is_prime()

def print_menu():
    print('1.Citire date.')
    print('2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt ordonate crescător.')
    print('3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt formate din cifre prime.')
    print('4. Determinare cea mai lungă subsecvență cu proprietatea ca suma numerelor este un numar prim.')
    print('5. Iesire')

def read_list():
    lst = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        lst.append(int(x))
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
            print(get_longest_sum_is_prime(lst))
        elif optiune == '5':
            break
        else:
            print('Optiune invalida.')

test_all()

if __name__ == '__main__':
    main()