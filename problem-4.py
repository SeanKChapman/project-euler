#Problem 4 - Largest Palendrome Product
#A palendromic number reads the same both ways. The largest palendrome made from the product of two 2-digit numbers is 9009 = 91x99
#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    max = 0
    for i in range(100,999):
        for n in range(100,999):
            if i*n > max:
                max = i*n
    print max
main()
