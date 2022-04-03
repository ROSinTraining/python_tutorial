import os
import time
from threading import Thread

OddSum = 0
EvenSum = 0

def findEven(start, end):
    global EvenSum
    for x in range(start, end, 1):
        if((x & 0) == 0):
            EvenSum += 1


def findOdd(start, end):
    global OddSum
    for x in range(start, end, 1):
        if((x & 1) == 0):
            OddSum += 1


if __name__ == '__main__':
    start = 0
    end = 190000

    t1 = Thread(target=findEven, args=(start, end,))
    t2 = Thread(target=findOdd, args=(start, end,))

    start_time = time.time()

    t1.start()
    t2.start()

    
    print(" --- Excution time: " + str(time.time() - start_time))

    print("Odd Sum: " + str(OddSum))
    print("Enven Sum: " + str(EvenSum))

    t1.join()
    t2.join()


# if __name__ == '__main__':
#     start = 0
#     end = 190000000
# 
#     start_time = time.time()
# 
#     findEven(start, end)
#     findOdd(start, end)
# 
#     print(" --- Excution time: " + str(time.time() - start_time))
# 
#     print("Odd Sum: " + str(OddSum))
#     print("Enven Sum: " + str(EvenSum))
