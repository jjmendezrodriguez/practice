#!/bin/python3

will_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def la_lista(will_list):
    new_list = []
    for i in will_list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list
    
        
jose_list = la_lista(will_list)

print(jose_list)

print(will_list is jose_list)

