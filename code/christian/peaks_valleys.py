data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(numbers):   #need to identify number with lower surrounding neighbors
    peak_list = []
    for x in range(1,len(numbers)-1):
        # print(x+5)
        if numbers[x] > numbers[x-1] and numbers[x] > numbers[x+1]: # cycles left and right of numbers
         peak_list.append(x)
    return peak_list


        
def valleys(numbers):   
    valley_list = []
    for x in range(1,len(numbers)-1):
        # print(x+5)
        if numbers[x] < numbers[x-1] and numbers[x] < numbers[x+1]:
            valley_list.append(x)
    return valley_list

# print(valleys(data))

def peaks_valleys(numbers): #add both peaks algorythim and valley algorythim using parenthesis and or between the two
    peaks_valley = []
    for x in range(1,len(numbers)-1):
        # print(x+5)
        if (numbers[x] > numbers[x-1] and numbers[x] > numbers[x+1]) or (numbers[x] < numbers[x-1] and numbers[x] < numbers[x+1]):
            peaks_valley.append(x)
    return peaks_valley
        
            



print(peaks_valleys(data))

        
























 