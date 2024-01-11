#!/usr/bin/env python3

def print_fibonacci(length):
    # print(list([]))
    if length < 1:
        indexes = list(range(length))
        print(indexes)
    elif length == 1:
        indexes = list(range(length))
        # print(indexes)
        print(indexes)
    elif length == 2:
        indexes = list(range(length))
        # print(indexes)
        print(indexes)
    else:
        # fibonacci always start with 0 and 1
        indexes=[0,1]

        for i in range(2, length):
            indexes.append(indexes[-1] + indexes[-2])
        print(indexes)


    

