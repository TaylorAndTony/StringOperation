def valid_caret(caret) -> bool:
    # ((())))
    lst = []
    lst.append(caret[0])
    for i in caret[1:]:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst[-1] == '(':
                lst.pop()
            else:
                lst.append(i)
    return len(lst) == 0


def valid_caret_2(caret):
    # )())()())
    # ((()))
    sum = 0
    for i in caret:
        if i == '(':
            sum += 1
        elif i == ')':
            if sum == 0:
                return False
            else:
                sum -= 1
    return sum == 0


print(valid_caret_2('((()))'))
print(valid_caret_2('))'))