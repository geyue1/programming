import random
import time

def timeGuess():
    print("start")
    interval = random.randint(1,10)
    time.sleep(interval)
    print("stop")
    guess_time = int(input("please enter guess time:"))
    if guess_time==interval:
        print("big win")
    elif -1<=guess_time-interval<=1:
        print("small win")
    else:print("lose")

timeGuess()