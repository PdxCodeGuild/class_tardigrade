9# Lab 9: Peaks and Valleys
# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# Visualization of test data:

data =	[1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
Index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# POI							P			V					P			V			
# Example I/O:

def peaks(data):
    peak= []
    for i in range(1, len(data)-1):
      if data[i] > data[i-1] and data[i] > data[i+1]:
        peak.append(i)
    return peak         
#print(peaks(data))



def valleys(data):
    valley = []
    for i in range(1, len(data)-1):
      if data[i] < data[i-1] and data[i] < data[i+1]:
        valley.append(i)
    return valley         
#print(valleys(data))

def peaks_and_valleys(peaks, valleys):
    pvlist= []
    valley_list= valleys(data)
    peak_list =peaks(data)

    for num in peak_list:
        pvlist.append(num)
    for num in valley_list:
        pvlist.append(num)
    pvlist.sort()
    
    # pvlist.append(valley_string)
    # pvlist.append(peak_string)
    
    return pvlist
print(peaks_and_valleys(peaks, valleys))