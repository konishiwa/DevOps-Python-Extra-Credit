# import the math module
import math
import sys
from fibo import fib


#pythagorean theorem solution:
def math_pythagoren(a,b):
    a = float(a)
    b = float(b)
    c = math.sqrt(a ** 2 + b ** 2)
    print(c)

#foobar text manipulation
def foobar_text():
     f = open("foobar.txt", "r")
     mystring = f.read()
     print(mystring.replace(',', '\n'))
     f.close()

#fib function
def fibonnaci():
    print(fib(1))

#sys arguments function:
def sys_arg(a, b):
    print("These are the variables: " + a + " " + b)

#while loop example:
def while_loop(x):
    while x > -1:
        x = x - 5
        print(x)

#python mitigation: https://semgrep.dev/docs/cheat-sheets/python-command-injection/


def main():
    math_pythagoren(3, 4)
    foobar_text()
    fibonnaci()

    print(sys.argv[0])
    print(sys.argv[1])
    sys_arg(sys.argv[0],sys.argv[1])
    while_loop(8)


main()