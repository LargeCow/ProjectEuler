
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(k)
    return inverse




if __name__ == '__main__':
    print('test')
    test = histogram('testtttt')
    print(test)
    inverse = invert_dict(test)
    print(inverse)
