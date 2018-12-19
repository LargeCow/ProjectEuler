

def ThreeAndFive(n):
    if n % 3 == 0:
        return n
    if n % 5 == 0:
        return n
    else:
        return False


def problem1(n_1):
    returnlist = list()
    for i in range(n_1):
        if ThreeAndFive(i) is not False:
            returnlist.append(i)
    value = sum(returnlist)
    return value

if __name__ == '__main__':
    test = problem1(1000)
    print(test)
