import time


def get_date(epoch_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))



print(get_date(1503455978))

print(time.time())