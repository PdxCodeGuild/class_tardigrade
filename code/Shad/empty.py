ist = []
Prime = []
def cc():
    
    while True:
        num = input( 'Enter your numbers:  \ntype fin when finsh')  
        ist.append(num)
        

        print(ist)
        return num

            # reverse the numbers in a list without the check digit.
       
    

         
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:


#list = []
#check_digit = list.pop(-1)
#new_list = check_digit
#reverse = check_digit.reverse()
#d = reverse[::2]
#double = d * 2
#sub = double[0:-1] - 9
#print(sub)
    