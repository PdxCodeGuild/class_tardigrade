# def peaks(data, n):
#     if n == 1:
#         return 0
#     if data[0] >= data[1]:
#         return 0
#     if data[n - 1] >= data[n - 2]:
#         return n - 1
#     for i in range(1, n - 1):
#         if data[i] >= data[i - 1] and data[i] <= data[i + 1]:
#             return i

# def valleys(data, n):
#     if n == 1:
#         return 0
#     if data[0] <= data[1]:
#         return 0
#     if data[n - 1] <= data[n - 2]:
#         return n - 1
#     for i in range(1, n - 1):
#         if data[i] <= data[i - 1] and data[i] <= data[i + 1]:
#             return i

# def peaks_and_valleys(peaks, valleys):
#     total_peaks_valleys = peaks.extend(valleys)
#     return total_peaks_valleys.sorted()

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# n = len(data)

# print(peaks_and_valleys(data, n))

"""ANOTHER VERSION"""

def peak(data, left = None, right = None):
    if left is None and right is None:
        left, right = 0, len(data) - 1
    
    mid = left + right // 2

    if (mid == 0 or data[mid - 1] <= data[mid] and mid == len(data) - 1 or data[mid + 1] <= data[mid]):
        return mid

    if mid - 1 >= 0 and data[mid - 1] > data[mid]:
        return peak(data, left, mid - 1)
        # return peak(data, mid + 1, right)

def peak_element(data):
    if not data:
        exit(-1)
    index = peak(data)
    return data(index)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(f"The peak element is {peak_element(data)}")

# def valleys(data, n):
#     if n == 1:
#         return 0
#     if data[0] <= data[1]:
#         return 0
#     if data[n - 1] <= data[n - 2]:
#         return n - 1
#     for i in range(1, n - 1):
#         if data[i] <= data[i - 1] and data[i] <= data[i + 1]:
#             return i

# def peaks_and_valleys(peaks, valleys):
#     total_peaks_valleys = peaks.extend(valleys)
#     return total_peaks_valleys.sorted()