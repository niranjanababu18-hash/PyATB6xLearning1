import time
def log(func):
    def wrapper():
        print("start of logs")
        func()
        print("end of logs")
    return wrapper

def time_log(func):
    def wrapper():
        start_time=time.time()
        #epoch time or unix time-time
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("total time:",end_time-start_time)
    return wrapper
@time_log
@log
def testui():
    print('First time')
    time.sleep(1)
@time_log
@log
def testui2():
    print('Second time')
    time.sleep(2)
testui()
testui2()
