#Peaks&Valleys


# """>>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def highs (numbers):
    """This function finds the peaks"""

    peak = []
    for i in range(1,(len(data))-1):
             if numbers[i-1]< numbers[i]> numbers[i+1]:   
                peak.append(i)
    return peak
print((highs(data)))

def lows (numbers):
    """This function finds the valleys"""
    valleys = []
    for i in range(1,(len(data))-1):
             if numbers[i-1]> numbers[i]< numbers[i+1]:   
                valleys.append(i)
    return valleys
print((lows(data)))

def peaks_valleys_combined (numbers):
    """This function finds the peaks and valleys in order of appearance"""
    all_peaks_valleys = []
    for i in range(1,(len(data))-1):
             if numbers[i-1]< numbers[i]> numbers[i+1]:   
                all_peaks_valleys.append(i)
                print("peaks")
             if numbers[i-1] > numbers[i] < numbers[i+1]:   
                all_peaks_valleys.append(i)
                print("valleys")   
    return all_peaks_valleys

print((peaks_valleys_combined (data)))

