import math #imports a bunch of math functions

x = 3.14

print(round(x)) #prints x rounded to the nearest whole integer
print(math.ceil(x)) #rounds a number up to the whole integer no matter what the decimal is
print(math.floor(x)) #rounds a number down to the whole number no matter what the decimal is
print(abs(x)) #prints the absolute value of a number: |x|
print(pow(x, 4)) #is an exponent number, returns x^4. The first perameter (lets call it x) is the base number. The second perameter (lets call it y) is the exponent number. It is x^y
print(math.sqrt(x)) #prints the square root of x.

a, b, c = 1, 2, 3

print(max(a, b, c)) #prints the biggest number out of the given numbers
print(min(a, b, c)) #prints the smallest number out of the given numbers