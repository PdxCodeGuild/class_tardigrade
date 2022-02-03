
from typing import List


def cc_valid( ):
    num_list = []
    string = input('enter: ')
    num_list=list(string)
    print(1, num_list)
    num_list.pop(-1)
    num_list.reverse()
    t = int(num_list[::2]) * 2
    print(2,t)
    for i in num_list:
        num_list[::2][i] * 2
        
        print(num_list[i])
    
    
    
    
    print(44,num_list)
    return num_list
    ist=[int(i) for i in input().split()]
    
    # del num_list[-1]
    # num_list.reverse()
List    
    
cc_valid()
