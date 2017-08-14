

def fib(max):

    a,b,n = 0,1,0

    while True:

        if  n<max :

            a, b = b, a + b

            yield a

            n += 1
        else:
            break

f = fib(10)

for i in range(10):
    print(f.__next__())