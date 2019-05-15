#!/usr/bin/env python3
from math import exp, log, sqrt
print("Output #1: I'm excited to learn Python.")

# 두 수를 더한다.
x = 4
y = 5
z = x + y

print("Output #2: Four plus five equals {0:d}.".format(z))

# 두 리스트를 더한다.
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))

print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5 * 4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.2f}".format(8.0/3))

print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

print("Output #14: {0:s}".format('I\'m enjoying learing Python.'))



