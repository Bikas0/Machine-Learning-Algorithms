import math as m


mod = int(input("Enter the modulus : "))
def calculate(n1,n2,n3,n4,n5,n6,mod):
    total = n1+n2+n3+n4+n5+n6
    r = total % mod
    result = factorial(r)
    re_fib = fib(total)
    return f"1: The modulus value is  {r}, 2: The second with {result} 3: The third with :{re_fib}"

def factorial(r):
    if r < 1:
        return 1
    fac=  r * factorial(r - 1)
    return fac

def fib(total):
    if total == 1 or total == 2:
        return 1
    fi =  fib(total - 1 ) + fib(total -2 )
    return fi

print(calculate(1,2,3,4,5,6,mod))