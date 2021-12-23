"""
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""
data_set = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def valleys(nums):
    for i in range(1, len(nums) - 1):
        if nums[i + 1] > nums[i] < nums[i - 1]:
            valley = i
            print(valley)

def peaks(nums):
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            peak = i
            print(peak)
peakorvalley = []
def peaks_and_valleys(nums):
    for i in range(1, len(nums) -1):
        if nums[i - 1] < nums[i] > nums[i + 1] or nums[i + 1] > nums[i] < nums[i - 1]:
            peakorvalley.append(i)

            print(peakorvalley)

valleys(data_set)
peaks(data_set)
peaks_and_valleys(data_set)