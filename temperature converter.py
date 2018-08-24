# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:48:31 2018

@author: haithama
"""
x = int(input("input temerature mode 1 for C to F and 2 for F to C "))
if x == 1:
    T = int(input("input celsius temerature "))
    if (T > -20 and T < 70):
        F = round((T + 40) * 9/5) - 40
        print("temperature in F is ", F)
        if F <= 32:
            print("very cold")
        elif (F > 32 and F <= 50):
            print("cold")
        elif (F > 50 and F <= 75):
            print("worm")
        elif F > 75:
            print("hot")
    else:
        print("temperature is out of range")
elif x == 2:
    T = int(input("input fahrenheit temerature "))
    if (T > -5 and T < 120):
        C = round((T + 40) * 5/9) - 40
        print("temperature in C is ", C)
        if C <= 0:
            print("very cold")
        elif (C > 0 and C <= 20):
            print("cold")
        elif (C > 20 and C <= 38):
            print("worm")
        elif C > 38:
            print("hot")
    else:
        print("temperature is out of range, try again")
else:
    print("wrong temperature mode selection, please re-enter your choice")