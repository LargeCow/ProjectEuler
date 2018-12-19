import random


def getDictObject(wordList):
    file = open(wordList, encoding='utf-8', errors='replace')
    return file



def passwordGen(wordList, lenCon):
    ## words = getDictObject(wordDict)
    final_pass = ''
    count = 0
    while True:
        res = ''
        word = wordList[random.randrange(len(wordList))]
        word = word.capitalize()
        quad_digit = random.sample(range(0,9), 4)
        for i in quad_digit:
            res += str(i)
        addition = word + str(res)
        final_pass += addition
        count += 1
        if len(final_pass) > lenCon and count >= 2:
            break
    return final_pass



if __name__ == '__main__':
    test = ['yes', 'no', 'Capitalize', 'Devil']
    pwd = passwordGen(test, 9)
    print(pwd)
