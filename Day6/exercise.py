#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
def second_symbol(s,symbol):
    index = -1
    lst = []
    for i in s:
        index = index + 1
        if i == symbol:
            lst.append(index)
    return lst[1]

    

print(second_symbol('hello world','l'))