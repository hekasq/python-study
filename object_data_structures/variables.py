# dynamic typing - unless specified, can reassign the variables
def variables_reassignment():
    sqrl = 1
    print(sqrl)
    sqrl = ["sqrl1", "sqrl2"]
    print(sqrl)


# pros : saves time; cons: errors
def variables_reassignment_conv():
    sqrt = int(1.3)
    print(sqrt)


def variables_typecheck():
    sqrl = ["sqrl1", "sqrl2"]
    print(type(sqrl))


if __name__ == '__main__':
    variables_reassignment()
    variables_reassignment_conv()
    variables_typecheck()
