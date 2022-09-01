def basic():
    print("BASIC: ")
    count = 3
    while count > 0:
        count -= 1
        print(f'count is {count}')
    else:
        print(f'And we\'re done')


def commands():
    print("COMMANDS: ")
    my_list = [1, 2, 3]
    for item in my_list:
        # does nothing, but keyword helpful to avoid errors
        pass
    for item in my_list:
        # continue - goes to the next iteration of loop
        if item == 3:
            continue
        print(item)
    for item in my_list:
        # break - breaks the loop
        if item == 2:
            break
        print(item)


if __name__ == '__main__':
    basic()
    commands()
