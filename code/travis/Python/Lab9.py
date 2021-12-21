"""
Lab 9:
Author: Travis Jackson
Date: 11/23/21
"""



terrain_data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks_list = []
valleys_list = []
peaks_and_valleys_list = []


# returns peaks
def peaks(terrain_data_list):

    for i, height_value in enumerate(terrain_data_list):    

        if i - 1 < 0: 

            continue

        if (i + 1) < len(terrain_data_list): 

            right_terrain_value = terrain_data_list[ i + 1 ]

        if i - 1 >= 0: 

            left_terrain_value = terrain_data_list[ i - 1 ] 

        #determines if a peak value
        if left_terrain_value == right_terrain_value \
            and height_value != left_terrain_value \
            and height_value > left_terrain_value:

            peaks_list.append(i)


    return peaks_list


#returns valleys
def valleys(terrain_data_list):

    for i, height_value in enumerate(terrain_data_list):    

        if i - 1 < 0: 

            continue

        if (i + 1) < len(terrain_data_list): 

            right_terrain_value = terrain_data_list[ i + 1 ]

        if i - 1 >= 0: 

            left_terrain_value = terrain_data_list[ i - 1 ] 

        #determines if in valley
        if left_terrain_value == right_terrain_value \
            and height_value != left_terrain_value \
            and height_value < left_terrain_value:

            valleys_list.append(i)

    return valleys_list


#returns peaks and valleys
def peaks_and_valleys(peaks_list, valleys_list):

    peaks_list.extend(valleys_list)
    peaks_and_valleys_list = peaks_list    
    peaks_and_valleys_list.sort()

    return peaks_and_valleys_list



#output
print(peaks(terrain_data_list))

print(valleys(terrain_data_list))

print(peaks_and_valleys(peaks_list, valleys_list))



#version 2

highest_value = 0
output_x = ""

#finds highest value
for i, height_value in enumerate(terrain_data_list):

    if height_value > highest_value:

        highest_value = height_value


# prints out values
for i in range(0, highest_value):

    for height_value in terrain_data_list:

        if height_value >= highest_value - i:

            output_x += "X "

        elif height_value != highest_value - i:

            output_x += "  "
        
    print(output_x)

    output_x = ''


