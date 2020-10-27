# Imporations

import os.path
import random

import threading
import time

# Fields

initialized: bool = False

random_list: list = []
reversed_list: list = []
nearly_sorted_list: list = []

threads: list = []


def callback(message: str) -> None:
    """
    This is a really simple callback.

    :param message: The message you want to send.
    :return: None
    """
    print(f"[Success] - {message}")


def selection_sorting(a_list: list) -> list:
    for i in range(len(a_list)):

        min_index = i
        for j in range(i + 1, len(a_list)):
            if (a_list[min_index] > a_list[j]):
                min_index = j

        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


def quick_sorting(a_list: list) -> list:
    if (len(a_list) < 1):
        return a_list
    else:
        selected = a_list.pop()

    higher_list = []
    lower_list = []

    for i in a_list:
        higher_list.append(i) if i > selected else lower_list.append(i)

    return quick_sorting(lower_list) + [selected] + quick_sorting(higher_list)


def quick_sort_executor(lst: list, list_name: str) -> None:
    new_list = quick_sorting(lst)
    create_file_if_not_exists("new_" + list_name, new_list)


def create_file_if_not_exists(name: str, values: list) -> None:
    path: str = name + ".txt"

    if (os.path.exists(path)):
        return
    else:
        file = open(path, "x")
        for value in values:
            file.write(str(value) + "\n")
        file.close()


def test_performance(code: threading.Thread) -> None:
    print(f"[Performance] Started testing '{code.name}'")
    start_millis = int(time.time() * 1000)

    # Start the actual thread/code
    code.start()

    print(f"[Performance] Test '{code.name}' took {int(time.time() * 1000) - start_millis}ms\n")


def initialize_lists() -> None:
    global initialized, random_list, reversed_list, nearly_sorted_list

    while (not initialized):
        random_list = [random.randint(0, 100) for _ in range(0, 10000)]

        reversed_list = [_ for _ in range(0, 10000)]
        reversed_list.reverse()

        for i in range(0, 10000):
            if (i % 10 == 0):
                nearly_sorted_list.append(random.randint(0, 10000))
            else:
                nearly_sorted_list.append(i)

        create_file_if_not_exists("random_list", random_list)
        create_file_if_not_exists("reversed_list", reversed_list)
        create_file_if_not_exists("nearly_sorted_list", nearly_sorted_list)
        initialized = True


def initialize_threads() -> None:
    threads.append(
        threading.Thread(
            target=initialize_lists,
            name="Initializing Lists"
        )
    )

    threads.append(
        threading.Thread(
            target=quick_sort_executor,
            name="Quick Sorting 'random_list'",
            args=(random_list, "random_list")
        )
    )

    threads.append(
        threading.Thread(
            target=quick_sort_executor,
            name="Quick Sorting 'reversed_list'",
            args=(reversed_list, "reversed_list")
        )
    )

    threads.append(
        threading.Thread(
            target=quick_sort_executor,
            name="Quick Sorting 'nearly_sorted_list'",
            args=(nearly_sorted_list, "nearly_sorted_list")
        )
    )


if __name__ == '__main__':
    initialize_threads()

    for thread in threads:
        if "Initializing Lists" not in thread.name:
            test_performance(thread)
            # test
        else:
            thread.start()
