import time

def k(upto):
    def collatz(n):
        if n < upto and lst[n] > 0:
            return lst[n]
        if n % 2 == 0:
            val = collatz(n/2) + 1
        else:
            val = collatz((3*n + 1)/2) + 2
        if n < upto:
            lst[n] = val
        return val

    lst = [0]*(upto*2)
    lst[1] = 1
    lst[0] = 1
    for i in range(upto):
        collatz(i)
    maximum= max(lst)
    return lst.index(maximum)

start_time = time.time()
print k(1000000)
print("--- %s seconds ---" % (time.time() - start_time))
