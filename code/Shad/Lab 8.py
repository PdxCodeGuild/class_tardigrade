
from typing import List


def cc_valid( ):
    num_list = []
    string = input('enter: ')
    num_list=list( string)
    num_list.pop(-1)
    num_list.reverse()
    t = num_list[::2] * 2
    print(t)
    for i in num_list:
        num_list[i][::2] * 2
        print(i)
        print(num_list[i])
    print(type(num_list))
    
    
    
    
    print(num_list)
    return num_list
    ist=[int(i) for i in input().split()]
    
    # del num_list[-1]
    # num_list.reverse()
List    
    
cc_valid()
