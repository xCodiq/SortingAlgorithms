import os.path
import threading
import time
import random as r

initialized: bool = False

rand_list: list = []
rev_list: list = []
near_sort_list: list = []


def sort_callback(message: str) -> None:
    """
    This is a really simple sort callback.

    :param message: The message you want to send.
    :return: None
    """
    print(f" [Callback] - {message}")


def quick_sort(lst: list) -> list:
    if (len(lst) < 1):
        return lst
    else:
        selected = lst.pop()

    higher: list = []
    lower: list = []

    for item in lst:
        if (item > selected):
            higher.append(item)
        else:
            lower.append(item)

    return quick_sort(lower) + [selected] + quick_sort(higher)


def init():
    global initialized, rand_list, rev_list, near_sort_list

    while (not initialized):

        rand_list = [r.randint(0, 50) for _ in range(0, 10000)]

        rev_list = [i for i in range(0, 10000)]
        rev_list.reverse()

        for i in range(0, 10000):
            if (i % 10 == 0):
                near_sort_list.append(r.randint(0, 10000))
            else:
                near_sort_list.append(i)

        initialized = True


def create_file(name: str, values: list) -> None:
    path: str = name + ".txt"

    if (not os.path.exists(path)):
        file = open(path, "x")
        for value in values:
            file.write(str(value) + "\n")
        file.close()


def test_performance(name: str, thread: threading.Thread) -> None:
    print(f"Started testing '{name}'")
    time_before = int(time.time() * 1000)

    # Start the actual thread
    thread.start()

    print(f" -> Test '{name}' took {int(time.time() * 1000) - time_before}ms\n")


def test(sleeptime: int, callback) -> None:
    """
    Target for the threads: sleep and call back with completion message.

    :param sleeptime: The sleeptime in seconds
    :param callback: The callback method
    :return: None
    """

    time.sleep(sleeptime)
    callback("%s completed!" % threading.current_thread().name)


if __name__ == '__main__':
    threads: list = []

    for i in range(0, 10):
        threads.append(
            threading.Thread(
                target=test,
                name="Thread #%d" % i,
                args=(10 - i, sort_callback)
            )
        )

    for thread in threads:
        t: threading.Thread = thread
        t.start()

# Test the performances of all the lists
# test_performance(name="init", thread=threading.Thread(target=init))
# test_performance(name="random_list", thread=threading.Thread(target=create_file, args=("random_list", rand_list)))
