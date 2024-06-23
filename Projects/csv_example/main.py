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

import pandas

data = pandas.read_csv("Projects/csv_example/weather_data.csv")
print(type(data))
# print(data["temp"])
