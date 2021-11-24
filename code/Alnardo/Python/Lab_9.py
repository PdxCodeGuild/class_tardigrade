#Lab 9 Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
list = []

def peaks():
    for i in range(len(data)):
        if i == 0 or i == (len(data)-1):
            continue
        elif data[i] > data[i - 1] and data[i] > data[i + 1]:
            print(i, 'Peaked')
# peaks()

def valleys():
    for i in range(len(data)):
        if i == 0 or i == (len(data)-1):
            continue
        elif data[i] < data[i - 1] and data[i] < data[i + 1]:
            print(i, 'Valleyed')
# valleys()
def peaks_and_valleys():
    for i in range(len(data)):
        if i == 0 or i == (len(data)-1):
            continue
        elif data[i] > data[i - 1] and data[i] > data[i + 1]:
            list.append(f'{i} is a peak')
            # print(i, 'this is a peak')
        elif data[i] < data[i - 1] and data[i] < data[i + 1]:
            list.append(f'{i} is a valley')
            # print(i, 'this is a valley')
    print(list)

for i in range(len(data)):
    # list.append(data[i])
    print(data[i], 'x' * data[i])

# print(list)
# peaks()
# valleys()
peaks_and_valleys()