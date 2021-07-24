s = 'ihfcbadeg'
list1 = list(s)


def isalphabetical_strings(t):
    if len(set(t)) != len(t):   # 排除有重复元素的情况
        return 'No'
    elif 'a' not in t:  # 排除不是从a开始的情况
        return 'No'
    else:  # 需要判断是否按序排开, 有三种情况
        pos = t.index('a')   # 定位
        while pos != t.index(max(t)):
            if pos == 0:  # pos在最左端的情况
                if ord(t[pos + 1]) != ord(t[pos]) + 1:
                    return 'No'
                else:
                    t.pop(pos)
            elif pos == len(t)-1:  # pos在最右端的情况
                if ord(t[pos - 1]) != ord(t[pos]) + 1:
                    return 'No'
                else:
                    t.pop(pos)
                    pos = pos-1
            else: # pos在中间的情况
                if ord(t[pos-1]) == ord(t[pos]) + 1:  # pos左移
                    t.pop(pos)
                    pos = pos - 1
                elif ord(t[pos+1]) == ord(t[pos]) + 1:  # pos右移,但由于pop指针位置不用动
                    t.pop(pos)
                else:
                    return 'No'
        return 'Yes'


print(isalphabetical_strings(list1))
