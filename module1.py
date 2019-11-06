"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code to print Fibonacci numbers

"""
n=10
x=[0,1]
for i in range(n-2):
    x=x+[x[i]+x[i+1]]

for i in range(n):
    print(x[i])
