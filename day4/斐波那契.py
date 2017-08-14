

def fib(max):

    a,b,n = 0,1,0

    while True:

        if  n<max :

            a, b = b, a + b

            print(a)

            n += 1
        else:
            break



fib(10)