#problema 2 : Cake-Candles
import sys

def birthdayCakeCandles(n, ar):
    
    ar.sort(reverse=True)

    max = ar[0]
    c = 0
    for objeto in ar:

        if max == objeto:
            c = c + 1

        else:
            break

    return c
