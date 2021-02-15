# Write a Javascript function that finds all prime numbers upto a number n.
# So if we call the function asfindPrimes(100), it should print all the prime numbers upto 100.
# Hints -
# 1.	You know how to check a number is prime or not. If you know it, doing the same for numbers from 1 to 100 is easy.
# 2.	If you have solved the problem using the first method above, please read about Sieve of Eratosthenes. It is a very efficient way to find all prime numbers upto n. And it is a common interview task to implement the same. Try and see if you can solve the program using that algorithm.

def primeNumber(n):
    if  n == 2 or n==3 :
        return n
    if n % 2 == 0 or n% 3 == 0:
        return
    return n
if __name__ == "__main__":
    n = 100
    l =[ ]
    for i in range(2, n+1):
        l.append(primeNumber(i))
    for j in l:
        if j == None:
            continue
        print(j,end=" ")
