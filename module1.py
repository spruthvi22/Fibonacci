"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Function to return Fibonacci numbers

"""
def Fibon(n):
    x=[0,1]
    for i in range(n-2):
        x=x+[x[i]+x[i+1]]
    return(x)
