def no_c(my_string):
    new_string = ''
    for k in my_string:
        if k in ['c', 'C']:
            continue
        new_string = new_string + k
    return new_string
