from ctypes import *

adder = CDLL('./adder.so')

print(adder.add_int(100,11))

add_int = adder.add_int

print(add_int(1,1))