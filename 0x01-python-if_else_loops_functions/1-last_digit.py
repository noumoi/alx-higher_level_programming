#!/bin/bash
import random
number = random.randint(-10000, 10000)
lastdigs = number % 10
if number >= 0:
    if lastdigs > 5:
        print("Last digit of {} is {} and\
    is greater than 5".format(number, lastdigs))
    elif lastdigs == 0:
        print("Last digit of {} is {} and\
is 0".format(number, lastdigs))
    
    else:
    
        print("Last digit of {} is {} and\

  is less than 6 and not 0".format(number, lastdigs))

    else:
    
        lastdigsneg = -number
  
        if lastdigsneg % 10 == 0:
        
            print("Last digit of {} is {} and\
            
  is 0".format(number, -(lastdisgneg % 10)))
  
        else:
        
            print("Last digit of {} is {} and\
            
  is less than 6 and not 0".format(number, -(lastdigsneg % 10)))
