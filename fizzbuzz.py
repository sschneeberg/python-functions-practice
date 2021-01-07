"""
Write a function called `fizzbuzz` that has a parameter `n`. `fizzbuzz` takes a numerical argument for the value of `n`, which is the maximum value to print up to. For example, if I gave you the number 10, I would expect your program to start at 1 and print up to 10.

Additionally, your function should do the following:

* If a number is divisible by 3, print `fizz`
* If a number is divisible by 5, print `buzz`
* If a number is divisible by 3 AND 5, print `fizzbuzz`
* If none of the above are true, just print the number itself
"""

def fizzbuzz(n):
    for m in range(1, n+1):
        if (m % 3 == 0 and m % 5 == 0): print('fizzbuzz')
        elif (m % 3 == 0): print('fizz')
        elif (m % 5 == 0): print('buzz')
        else: print(m)
    return

fizzbuzz(20)

def alt_fizzbuzz(n):
    for m in range(1, n+1):
        print('fizzbuzz' if (m % 3 == 0 and m % 5 == 0) 
            else 'fizz' if (m % 3 ==0 ) 
            else 'buzz' if (m % 5 == 0) 
            else m)
    return

alt_fizzbuzz(20)

def shorter_fizzbuzz(n):
    for m in range(1, n+1):
        print ('fizz'*(m % 3 == 0) + 'buzz'*(m % 5 == 0) or m)
    return

shorter_fizzbuzz(20)