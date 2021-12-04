import datetime
# open lab24_rain_data.txt using with open command
file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/lab24_rain_data.txt"

with open(file_path, "r") as file:
    rain_data_lines = file.read().split(",")
print(rain_data_lines)



# date = datetime.datetime.strptime("25-MAR-2016", "%d-%b-%Y")
# print(date.year) # 2016
# print(date.month) # 3
# print(date.day) # 25
# print(date) # 2016-03-25 00:00:00
# print(date.strftime("%d-%b-%Y")) # 25-Mar-2016