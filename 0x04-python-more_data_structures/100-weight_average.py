#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    top = 0
    bot = 0

    for tup in my_list:
        top += tup[0] * tup[1]
        bot += tup[1]

    return (top / bot)
