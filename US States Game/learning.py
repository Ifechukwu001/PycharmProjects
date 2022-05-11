# # import csv
# #
# # with open("weather.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
# import math
#
# data = pandas.read_csv("weather.csv")
#
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# #
# # avg = 0
# #
# # avg = sum(temp_list) / len(temp_list)
# # # print(avg)
# #
# # max_temp = data["temp"].max()
# # print(max_temp)
#
# # print(data[data.temp == 24])
#
# monday= data[data.day == "Monday"]
# mon_temp = monday.temp

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = squirrel_data["Primary Fur Color"]
gray_color = 0
black_color = 0
cinnamon_color = 0

"""Item,value was used to iterate over the fur_color.items(), because the function ".items()" iterates over the 
fur_color series and returns a list of tuples in the form of [(index1,value1), (index2,value2),...,(indexi,valuex)j]"""
for item, value in fur_color.items():
    if value == "Gray":
        gray_color += 1
    elif value == "Cinnamon":
        cinnamon_color += 1
    elif value == "Black":
        black_color += 1

fur_dict = {
    "Fur color": ["gray", "red", "black"],
    "Count": [gray_color, cinnamon_color, black_color],
}

squirrel_final_data = pandas.DataFrame(fur_dict)
squirrel_final_data.to_csv("squirrel_count.csv")
