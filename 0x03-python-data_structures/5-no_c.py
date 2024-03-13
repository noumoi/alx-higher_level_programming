#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for j in my_string:
        if j in ['c', 'C']:
            continue
        new_string = new_string + j
    return new_string
