# Imporations

import os.path
import random
import sys

import threading
import time

# Fields

initialized: bool = False

random_list: list = []
reversed_list: list = []
nearly_sorted_list: list = []

threads: list = []

# Settings
sys.setrecursionlimit(1000000)


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
    """
    Create a file if it does not exist of a selection sorted list

    :param lst: the list the program should use to sort using selection sorting
    :param list_name: the list name the program should use for creating the file path
    :return: None
    """

    if (len(lst) < 1):
        pass

    new_list = quick_sorting(lst)
    create_file_if_not_exists("new_" + list_name, new_list)


def selection_sort_executor(lst: list, list_name: str) -> None:
    """
    Create a file if it does not exist of a selection sorted list

    :param lst: the list the program should use to sort using selection sorting
    :param list_name: the list name the program should use for creating the file path
    :return: None
    """

    if (len(lst) < 1):
        pass

    new_list = selection_sorting(lst)
    create_file_if_not_exists("new_" + list_name, new_list)


def create_file_if_not_exists(name: str, values: list) -> None:
    """
    Create a file if it does not exist yet. Files will be stored directly in the project source.
    NOTE: This function will automatically add '.txt' to the path.

    :param name: the name of the file you want to create
    :param values: the values the program should put in the created file
    :return: None
    """
    path: str = name + ".txt"

    if (os.path.exists(path)):
        return
    else:
        file = open(path, "x")
        for value in values:
            file.write(str(value) + "\n")
        file.close()


def test_performance(code: threading.Thread) -> None:
    """
    Test a threading.Thread with built in logging messages. Timestamp is in millis

    :param code: the threading.Thread to test
    :return: None
    """
    print(f"[Performance] Started testing '{code.name}'")
    start_millis = int(time.time() * 1000)

    # Start the actual thread/code
    code.start()

    print(f"[Performance] Test '{code.name}' took {int(time.time() * 1000) - start_millis}ms\n")


def initialize_lists() -> None:
    """
    This is the most important function of the entire program. This function is used to initialize the list and
    fill the global variables with values. Make sure you fire this function on startup before starting the threading.

    :return: None
    """
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


def initialize_quick_sorting_threads() -> None:
    """
    Initialize the quick sorting threads and add them to the threads list

    :return: None
    """
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


def initialize_selection_sorting_threads() -> None:
    """
    Initialize the selection sorting threads and add them to the threads list

    :return: None
    """
    threads.append(
        threading.Thread(
            target=selection_sort_executor,
            name="Selection Sorting 'random_list'",
            args=(random_list, "random_list")
        )
    )

    threads.append(
        threading.Thread(
            target=selection_sort_executor,
            name="Selection Sorting 'reversed_list'",
            args=(reversed_list, "reversed_list")
        )
    )

    threads.append(
        threading.Thread(
            target=selection_sort_executor,
            name="Selection Sorting 'nearly_sorted_list'",
            args=(nearly_sorted_list, "nearly_sorted_list")
        )
    )


if __name__ == '__main__':
    """
    This will be used to start the program. Comment out what type of sorting you don't want to use.
    At the moment you are only able to have one sorting type enabled at the time.
    
    Date: 28 Oct 2020
    """
    initialize_lists()
    initialize_selection_sorting_threads()
    # initialize_quick_sorting_threads()

    [test_performance(thread) for thread in threads]
