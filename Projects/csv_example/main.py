"""Module to demonstrate how to open and use CSV files."""

# data = []

# with open("Projects/csv_example/weather_data.csv", encoding="utf-8") as file:

#     content = file.readlines()

#     for lines in content:
#         data.append(lines.strip())

# import csv

# with open("Projects/csv_example/weather_data.csv", encoding="utf-8") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)

# data = pandas.read_csv("Projects/csv_example/weather_data.csv")
# # print(type(data))
# # # print(data["temp"])

# data_dic = data.to_dict()

# temp_list = data['temp'].to_list()

# # print(data['temp'].max())

# # # Get data in columns

# # print(data.condition)

# # Get data in row

# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']

# print((monday.temp * 9/5)+32)

# Create a dateframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)

# data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv(
    "Projects/csv_example/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240623.csv"
)

gray_count = len(data[data['Primary Fur Color'] == "Gray"])
red_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_count = len(data[data['Primary Fur Color'] == "Black"])

color_dict = {
    "colors": ["gray", "red", "black"],
    "count": [gray_count, red_count, black_count]
}

final_df = pandas.DataFrame(color_dict)

final_df.to_csv('Projects/csv_example/squirrel_count.csv')