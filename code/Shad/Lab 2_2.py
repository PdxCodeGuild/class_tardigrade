# input form user
# done or int
# if int collect in list
# if done break
# list 


d=[]
sum = 0

while True:
    
    user= input("enter a number, or 'done': ")
    
    if user == 'done':
        break
    else:
        d.append(int(user))
         
print(d)
running_sum = 0
t = len(d)

for num in d:
    running_sum = running_sum + num
    print(num, "elements in nums list")
    print(running_sum)
#end for loop
result = running_sum/t
print(result)
    #print(result)
 
