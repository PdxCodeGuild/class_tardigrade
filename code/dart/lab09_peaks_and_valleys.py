def peaks(n, nums: list[int]):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + right // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else: 
            left = mid + 1
    return left

def valleys(data, n):
    if n == 1:
        return 0
    if data[0] <= data[1]:
        return 0
    if data[n - 1] <= data[n - 2]:
        return n - 1
    for i in range(1, n - 1):
        if data[i] <= data[i - 1] and data[i] <= data[i + 1]:
            return i

def peaks_and_valleys(peaks, valleys):
    total_peaks_valleys = peaks.extend(valleys)
    return total_peaks_valleys.sorted()

nums = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
n = len(nums)

print(peaks_and_valleys(nums, n))