#Problem 5

pt = 1000

def solve():
    for a in range (1,1000):
        for b in range (a + 1,1000):
            c = pt - b - a
            if a**2 + b**2 == c**2 and a + b + c == pt:
                pr = a * b * c
                print(pr)
                print(a,b,c)