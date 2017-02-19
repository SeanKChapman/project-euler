#Problem 5 - Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#What is the smallest positive number that is evenly divisible  by all the numbers from 1 to 20

import math
def main():
    #print (2**4 * 3**2 * 5*7*11*13*17*19)

    #for i in range(1,20):
    #    allPrimes(i)
    for i in range(1,20):
        findPrimes(i)

#Returns a list of all prime numbers less than n
def allPrimeFactors(n):
    primes = []
    nRange = []
    for i in range(0,n):
        nRange.append(True)
    for i in range(2, (int)(round(n**0.5))):
        if nRange[i] == True:
            j = 2
            num = 0
            while j < n:
                nRange[j] = False
                j = i**2 + num*i
                num = num+1
    for i in range(len(nRange)):
        if nRange[i] == True:
            primes.append(i)
    print primes

def allPrimes(n):
    primes = []
    primeFactors = []
    for i in range(1,n+1):
        if (i==2 or i==3 or i==5 or i==7) or not(i%2==0 or i%3==0 or i%5==0 or i%7==0):
            primes.append(i)
    print primes

    for i in range(len(primes)):
        if n % primes[i] == 0:
            primeFactors.append(primes[i])
    print primeFactors

def findPrimes(n):
    primeFactors = []
    primeFactors.append(1)
    for i in range(1, n+1):
        if n >=10:
            if n%2 == 0:
                primeFactors.append(2)
                n /= 2
            if n%3 == 0:
                primeFactors.append(3)
                n /= 3
            if n%5 == 0:
                primeFactors.append(5)
                n /= 5
            if n%7== 0:
                primeFactors.append(7)
                n /= 7
    if isPrime(i):
        primeFactors.append(i)
    print i, isPrime(i), primeFactors

def isPrime(n):
    if n < 10:
        if n == 1 or n == 2 or n ==3 or n==5 or n ==7:
            return True
        else:
            return False
    if n >= 10:
        if n%2==0 or n%3==0 or n%5==0 or n%7==0:
            return False
        else:
            return True
main()


''' -- Brute Force -- Takes Forever ---
    i = 20
    done = False
    while done == False:
        if (i%1==0 and i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0
            and i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0):
            done = True
        else:
            i = i+20
            print i
'''
