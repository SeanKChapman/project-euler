#Problem 2 - Even Fibonacci Numbers
#By considering the terms in the fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

def main():
    print(fib(100))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: return fib(n-1) + fib(n-2)
main()
