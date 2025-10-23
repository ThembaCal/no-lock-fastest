import pandas as pd
# from bs4 import BeautifulSoup
# import csv

# file = open('index.html', 'r')

# soup = BeautifulSoup(file, 'lxml')

# car_content = soup.select('div.item-info')

# data = []

# for car in car_content:
#     name = car.select_one('h3')
#     tag = car.find("span")

#     values = car.select('span.field-value')
#     div = car.find('div', class_='article-info')
#     try:
#         vehicle_class = div.find(string=True, recursive=False).split('-')[0].strip() #type: ignore
#     except AttributeError:
#         vehicle_class = None

#     car_info = {
#         'Name': name.text.strip() if name else None,
#         'Class': vehicle_class,
#         'Top Speed': values[1].text.strip()  if len(values) > 1 else None,
#         'Price': values[0].text.strip()  if len(values) > 0  else None,
#     }

#     data.append(car_info)

# # print(data)
# fieldnames = list(data[0].keys())

# with open('output.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

file = open("output.csv", 'r')

table = pd.read_csv(file)
print(table.filter(['class']))