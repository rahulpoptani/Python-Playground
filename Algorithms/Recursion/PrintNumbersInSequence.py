def f(n):
    if n == 0:
        return
    print(n)
    f(n - 1)
    print(n)

f(3)

'''
What happens conceptually
-----------------------------------
f(3) enters → prints 3
Calls f(2) → pauses f(3)
f(2) prints 2
Calls f(1) → pauses f(2)
f(1) prints 1
Calls f(0)
f(0) hits base case → returns

Now stack unwinds:
f(1) prints 1
f(2) prints 2
f(3) prints 3
'''