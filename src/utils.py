import time

MILLI_SECS_IN_DAY = 86400000


def get_date(epoch_time_millis):
    """ Given an epoch time in milli seconds, returns the corresponding date. """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time_millis / 1000))


def open_file(filepath):
    """ Opens the file located at the given filepath and returns a string of its contents. """
    with open(filepath, 'r') as file:
        return file.read().replace('\n', '')


def days_ago(last_time):
    today = time.time() * 1000
    dt = today - last_time
    return dt / MILLI_SECS_IN_DAY

if __name__ == '__main__':
    last_time = 1502656380769
    print(get_date(last_time))
    print (days_ago(last_time))
