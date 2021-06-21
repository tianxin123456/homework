import re


def secondHighest(s):
    num1 = re.findall(r'[0-9]', s)
    num2 = [int(x) for x in num1]
    r1 = list(set(num2))
    r1.sort()
    if len(r1) > 1:
        return r1[-2]
    else:
        return -1


print(secondHighest('dfa12321afd'))
