def get_temp(temp, grad1, grad2):
    '''

    :param temp: temperatura ce trebuie convertita
    :param grad1: unitatea de masura initiala
    :param grad2: unitatea de masura convertita

    '''
    if grad1 == 'C':
        if grad2 == 'K':
            temp = temp + 273.15
            return temp
        elif grad2 == 'F':
            temp = (temp * 9 / 5) + 32
            return temp
        elif grad2 == 'C':
            return temp
    if grad1 == 'F':
        if grad2 == 'K':
            temp = (temp - 32) * 5 / 9 + 273.15
            return temp
        elif grad2 == 'F':
            return temp
        elif grad2 == 'C':
            temp = (temp - 32) * 5 / 9
            return temp
    if grad1 == 'K':
        if grad2 == 'K':
            return temp
        elif grad2 == 'F':
            temp = ((temp - 273.15) * 9 / 5) + 32
            return temp
        elif grad2 == 'C':
            temp = temp - 273.15
            return temp


def test_get_temp():

    assert get_temp(10, 'a', 'C') is None
    assert get_temp(100, 'C', 'K') == 373.15
    assert get_temp(123, 'C', 'F') == 253.4
    assert get_temp(0, 'F', 'c') is None
    assert get_temp(20, 'K', 20) is None
    assert get_temp(432, 'k', 'F') is None
    assert get_temp(100, 'C', 'F') == 212
    assert get_temp(20, 'k', 'c') is None


def cmmdc(x, y):
    # Calculeza cel mai mic divizor comun al numerelor x si y introduse  ca parametrii
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    return x


def cmmmmc(x, y):
    # Calculeaza si determina cel mai mare multiplu comun al numerelor x,y
    return (x * y) // cmmdc(x, y)


def get_cmmmc(lista):
    # Determina cmmmc-ul a n numere introduse intr o lista
    n = len(lista)
    c = cmmmmc(lista[0], lista[1])
    for i in range(2, n):
        c = cmmmmc(c, lista[i])
    return c


def test_get_cmmmc():
    assert get_cmmmc([4, 6, 8]) == 24
    assert get_cmmmc([5, 12, 4]) == 60
    assert get_cmmmc([3, 8, 9]) == 72


def main():
    while True:
        print('1. Conversie temperatura.')
        print('2. CMMMC a n numere.')
        print('x. Ieșire din program')
        optiune = input('Alege optiune: ')
        if optiune == '1':
            temp = float(input('Introduceti temperatura: '))
            grad1 = input('Introduceti tipul de grad: ')
            grad2 = input('Introduceti in ce grad vreti sa convertiti: ')
            conversie = get_temp(temp, grad1, grad2)
            print(f'Conversia a {temp} {grad1} in {grad2} este {conversie}.')
        elif optiune == '2':
            numere_str = input("Introduceti numerele: ")
            numere_str = numere_str.split(' ')
            lista_nr = []
            for numar in numere_str:
                lista_nr.append(int(numar))
            rezultat = get_cmmmc(lista_nr)
            print(f'Cmmmc ul numerelor introduse este: {rezultat}.')
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


test_get_temp()
test_get_cmmmc()
main()
