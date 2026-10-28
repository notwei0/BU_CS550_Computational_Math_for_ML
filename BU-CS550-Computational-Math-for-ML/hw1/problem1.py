#Problem 1

import timeit

def solve():
    for b in range(140, 161):
        for a1 in range(20, 41):
            for a2 in range(80, 101):
                for a3 in range(100, 121):
                    for a4 in range(120, 141):

                        if a1**5 + a2**5 + a3**5 + a4**5 == b**5:
                            print(f"a1={a1}, a2={a2}, a3={a3}, a4={a4}, b={b}")
                            return

time = timeit.timeit(solve, number=1)
print(f"{time} seconds".format(str(time)))