def list_iterator():
    strings = ['a', 'b', 'c']
    more_strings = ['e', 'f']
    strings.append('d')
    strings.extend(more_strings)

    print(strings)

    for str in strings:
        if str.startswith('a'):
            print('found a')
        if str.startswith('b'):
            str += 'ohno'
            print(str)
            str = str.removeprefix('b')
            print(str)
        if str.startswith('c'):
            str += 'derp'
            print(str[-2])
        if str.startswith('d'):
            str += 'yay'


def dict_iterator():
    my_dic = {'a': 'b', 'c': 'd'}
    revised = {}
    for k, v in my_dic.items():
        print(k, v)
    revised = {k: v for k, v in my_dic.items() if 'a' in k}
    print(revised)
    print(my_dic['a'])
    for k in my_dic.keys():
        print(k)


if __name__ == '__main__':
    # list_iterator()
    dict_iterator()
