import time


def counter(t):
    while t:
        min, sec = divmod(t, 60)
        timer = "{:02d} : {:02d}".format(min, sec)
        print(timer)
        time.sleep(1)
        t -= 1
    print("completed")


x = input("enter the value ")
counter(int(x))
