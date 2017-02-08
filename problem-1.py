#Problem 1 - Multiples of 3 and 5
#Find the sum of all the multiples of 3 and 5 below 1000

def main():
    x = 0
    for i in range(1000):
        if(i%3 or i%5):
            x = x+i
    print x;
main()
