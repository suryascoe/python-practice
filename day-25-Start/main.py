# with open("weather_data.csv", 'r') as csv_data:
#     content = csv_data.readlines()
#     print(content)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create Dataframe

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_counts.csv")
