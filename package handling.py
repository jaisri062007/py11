#factorial package/fac.py file
def factorial(n):
        fact = 1
        if n < 0:
                return "Factorial not possible"
        for i in range(1, n + 1):
                fact = fact * i
        return fact
#combination package/com.py file
from factorial.fac import factorial
def ncr(n, r):
        result = factorial(n) / (factorial(r) * factorial(n-r))
        return result
def npr(n, r):
        result = factorial(n) / factorial(n-r)
        return result
#main program
from combination.com import ncr, npr
n = int(input("Enter n value: "))
r = int(input("Enter r value: "))
print("nCr =", ncr(n, r))
print("nPr =", npr(n, r))
