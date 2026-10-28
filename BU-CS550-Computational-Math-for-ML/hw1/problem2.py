#Problem 2

lp = 0

for x in range(1,100):
    for y in range(100,1000):
        palindrome = x * y
        palindrome_string = str(palindrome)

        if palindrome_string == palindrome_string[::-1]:
            if palindrome > lp:
                lp = palindrome
print(lp)