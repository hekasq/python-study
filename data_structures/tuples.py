def query_tuple():
    tuple = (1, "two", 3, 3)
    lenght = len(tuple)
    idx = tuple.index("two")
    count = tuple.count(3)
    print(tuple)


def converstion_iteration():
    list_1 = [1, 2, 3, 3]
    tuplez = tuple(list_1)

    zipped = zip([1, "two", 3], list_1)
    #zipped is an iterator. It will match the elements of the list into tuples, e.g. (1,1),(2,"two") discarding what it cannot match
    for i in zipped:
        print(i)
    #mapped is an iterator
    mapped = map(lambda x: x + 2, list_1)
    for i in mapped:
        print(i)

    #convert tuple to list and back
    temp_list = list(tuplez)
    temp_list.insert(1, 'a')  # Insert 'a' at position 1
    my_tuple = tuple(temp_list)

    print(my_tuple)

def init_tuple():
    tuple = (1, 2, 3)
    print(tuple)


if __name__ == '__main__':
    converstion_iteration()
