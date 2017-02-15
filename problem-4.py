#Problem 4 - Largest Palendrome Product
#A palendromic number reads the same both ways. The largest palendrome made from the product of two 2-digit numbers is 9009 = 91x99
#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    allPalindromes = []
    for i in range (100,999):
        for j in range(i, 999):
            product = i*j
            if checkPalindrome(product) == True:
                allPalindromes.append(product)
    print max(allPalindromes)

def checkPalindrome(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n  = n // 10
    isPalindrome = True
    for i in range(len(digits)/2):
        if digits[i] != digits[len(digits) - i -1]:
            isPalindrome = False
            break

    if isPalindrome == True:
        #print digits
        return True



main()
