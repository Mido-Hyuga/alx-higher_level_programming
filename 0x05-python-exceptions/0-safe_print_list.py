#!/usr/bin/python4
def safe_print_list(my_list=[], x=0):
    cmp = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            cmp += 1
        except IndexError:
            break
    print("")
    return cmp
