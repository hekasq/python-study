def readFile():
    print("BASIC: ")
    # can use full filepath or just name if in same dir
    timestampsfile = open('timestamps')
    contents = timestampsfile.read()
    # reset cursor
    timestampsfile.seek(0)
    contents = timestampsfile.readlines()
    print(contents)
    timestampsfile.close()


def readFileCorrectly():
    print("CORRECT: ")
    with open('timestamps') as ts_file:
        content = ts_file.readlines()
        print(content)


# modes: r -read only, w - write only, a = a[[end only, r+ -read/write, w+ read, wriet, overwrites
def readFileMethods():
    print("WITH MODES: ")
    with open('timestamps-output', mode='w') as ts_file:
        content = ts_file.write('hi\n')
        print(content)


def addNewLine():
    print("WITH ADD NEW LINE: ")
    with open('timestamps-output', mode='a') as ts_file:
        ts_file.write('derp|mrf|fnar')


def iterateThroughFileLines():
    print("ITERATING: ")
    with open('timestamps', mode='r') as ts_file:
       for line in ts_file:
          content = line[:-1].split("|")
          cid=content[2]
          timestamp = content[0]
          action=content[1]
          print('eol')
   #C6FCEC7F62FBEA16-0000000000000019 - 1660868851- 1660868850 - 4.5 hours - reason


if __name__ == '__main__':
    readFile()
    readFileCorrectly()
    readFileMethods()
    addNewLine()
    iterateThroughFileLines()
