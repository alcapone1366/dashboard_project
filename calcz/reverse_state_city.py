import reverse_geocode
import pandas as pd


dataframe = pd.read_csv("./betterFormat.csv")

lat_list = dataframe["Lat"].tolist()
lon_list = dataframe["Lon"].tolist()
# print(lat_list[:30])
# print(lon_list[:30])

my_tuple = list(zip(lat_list, lon_list))

# print(my_tuple[:30])

for i in my_tuple:
    print(i,"\n")

print(len(my_tuple))

ready_for_csv = reverse_geocode.search(my_tuple)
print(ready_for_csv[:30])
cities = [i["city"]for i in ready_for_csv]
print(cities[:19])

print(len(cities))

dataframe["my_cities"] = cities

added_cities = dataframe.to_csv("./added_cities.csv")