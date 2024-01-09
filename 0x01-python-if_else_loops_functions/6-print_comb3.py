#!/usr/bin/python3
for g in range(1, 89):
    if (g % 10 > g / 10):
        print('{:02d}, '.format(g), end='')
print(89)
