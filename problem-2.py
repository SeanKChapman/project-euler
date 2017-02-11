#Problem 2 - Even Fibonacci Numbers
#By considering the terms in the fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

from math import sqrt
def main():
    #Initialize variables
    sum = 0
    i = 1;

    #Between 0-100, check if the i'th term if the fibonacci sequence is even and below 4 million
    #If it is, add it to the sum
    for i in range(100):
        if int(fib(i)) % 2 == 0 and fib(i) <= 4000000:
            sum = sum + fib(i)
            
    #After loop is complete, print sum
    print(sum)

#Returns the n'th term of the fibonacci sequence
def fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
main()
