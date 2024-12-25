import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)-9
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        root_1 = root ** 0.5
        root_2 = - root ** 0.5
        result.append(root_1)
        result.append(root_2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0.0:
            root_3 = root1 ** 0.5
            root_4 = - root1 ** 0.5
            result.append(root_3)
            result.append(root_4)
        elif root1 == 0.0:
            result.append(root1)
        if root2 > 0.0:
            root_5 = root2 ** 0.5
            root_6 = - root2 ** 0.5
            result.append(root_5)
            result.append(root_6)
        elif root2 == 0.0:
            result.append(root2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0],  roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()
