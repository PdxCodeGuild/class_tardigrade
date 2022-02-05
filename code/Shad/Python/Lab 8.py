

from operator import index
from pprint import pprint

from typing import List


def cc_valid( ):
    num_list = []
    string = input('enter: ')
    num_list=list(string)
    num_list.pop(-1)
    num_list.reverse()
    print(num_list)
    
    
    for i , num in enumerate(num_list):
        # print('i',i)
        # print('num',num)
        # print("test",i%2)
        num_list[i] = int(num)

        if i % 2  == 0:
           num_list[i] = int(num) * 2
           print(num_list[i])

    for i , num in enumerate(num_list):
        
        if num > 9:
            num_list[i] = num - 9
            print(num_list)
    sum = 0
    valid=[]
    for num in range(0, len(num_list)):
        sum = sum + num_list[num]
        sec= valid.append(sum)
        print(num_list)

        
    valid =valid[-1]
    print(valid)

    
    digitsec = [int(a) for a in str(valid)]
    new_valid=digitsec[-1]
      
    print('valid',new_valid)
    
       
        
                
        
    


    
     
    
    
    
    ist=[int(i) for i in input().split()]
    
    # del num_list[-1]
    # num_list.reverse()
List    
    
cc_valid()
