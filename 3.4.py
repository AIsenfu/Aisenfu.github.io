# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
x=6==4,5
print(x)
a=int(input())
print(a==3,4)

print([3]in[1,2,3,4])

print(list(range(10,1,-3)))
print(sorted([1, 2, 3], reverse=True))
print({1:'a', 2:'b', 3:'c'}.get(4, 'd'))
d=dict(name='dong',age='39')
print(d['name'])
print({1, 2, 3, 4} - {3, 4, 5, 6})
x=[3, 5, 7]
print(x[10:])
s={1,2,3}
b={1,2,3,4,5,6}
print(s<b)
print( {1, 3, 2} > {1, 2, 3} )
time.sleep(5)