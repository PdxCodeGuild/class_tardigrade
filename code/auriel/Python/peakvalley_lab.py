data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(peaks):
    peak_list = []
    for i in range(1, len(peaks) -1): # Range is 1, -1 due to numbers in list can be any positive number
        num = peaks[i]
        if num > peaks[i - 1] and num > peaks[i + 1]: # If num has a lower number on both sides
            peak_list.append(i)
    return peak_list

def valleys(valleys):
    valleys_list = []
    for i in range(1, len(valleys) -1): # Range is 1, -1 due to numbers in list can be any positive number
        num = valleys[i]
        if num < valleys[i - 1] and num < valleys[i + 1]: # If num has a higher number on both sides
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(peaks_valleys):
    peaks_ls = peaks(data)
    valleys_ls = valleys(data)
    print(sorted(peaks_ls + valleys_ls))

peaks_and_valleys(data)