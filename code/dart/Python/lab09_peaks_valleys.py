
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

index = 0
peaks = []
valleys = []
peaks_and_valleys = []
largest_number = 0

for i in range(1, len(data) - 1):
    if data[i + 1] < data[i] > data[i - 1]:
        index += 1
        peaks.append(i)

for i in range(1, len(data) - 1):
    if data[i+ 1] > data[i] < data[i- 1]:
        index += 1
        valleys.append(i)

for i in range(1, len(data) - 1):
    if data[i + 1] > data[i] < data[i - 1] or data[i + 1] < data[i] > data[i - 1]:
        index += 1
        peaks_and_valleys.append(i)

print(f"Peaks: {peaks}")
print(f"Valleys: {valleys}")
print(f"Peaks and valleys: {peaks_and_valleys}")