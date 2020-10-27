import time

rand_list = [8, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5, 6, 3, 6, 7, 1, 4, 7, 8, 9, 1, 0, 1, 0, 9, 3, 7, 3, 7, 6, 9, 2, 8, 7, 6, 3, 5]

print()


def selection_sort(a_list: list):
    for i in range(len(a_list)):

        min_index = i
        for j in range(i + 1, len(a_list)):
            if (a_list[min_index] > a_list[j]):
                min_index = j

        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


def quick_sort(a_list: list):
    if (len(a_list) < 1):
        return a_list
    else:
        selected = a_list.pop()

    higher_list = []
    lower_list = []

    for i in a_list:
        higher_list.append(i) if i > selected else lower_list.append(i)

    return quick_sort(lower_list) + [selected] + quick_sort(higher_list)


start_millis = time.time()

print(rand_list)
print(selection_sort(rand_list))
print(quick_sort(rand_list))

# print(f"\n\t»»\tApplication took {(int(round(time.time() * 1000)) - start_millis)}ms")

# class TestError(Exception):
#
#     def __init__(self, tpe: str = "Unknown"):
#         self.tpe = tpe
#         # TestError.handle(self)
#
#     def handle(self):
#         print("Something went wrong while sorting a list. Please make sure you have a valid list with integers only!")
#
#
# boolean = True
#
# if (boolean):
#     try:
#         raise TestError
#     except TestError as e:
#         e.handle()
#
print(f"\n\t»»\tApplication took: {(time.time() - start_millis)}")
