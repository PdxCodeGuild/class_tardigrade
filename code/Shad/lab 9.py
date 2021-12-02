9# Lab 9: Peaks and Valleys
# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# Visualization of test data:

Data =	[1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
Index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# POI							P			V					P			V			
# Example I/O:

def peaks(Data):
    for p in range(len(Data[1:19]), len(Index)):
        if Data[p] >= Data[1:19]:
            print( p ) 
        return (p)


peaks( Data)
