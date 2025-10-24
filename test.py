from bs4 import BeautifulSoup


file = open('index.html', 'r')

soup = BeautifulSoup(file, 'lxml')

car_content = soup.select('div.item-info')

# print(car_content)

for car in car_content:
    name = car.select_one('span.badge')
    tag = car.find("span")
    speed = car.select('span.field-value')[1]
    price = car.select('span.field-value')[0]
    div = car.find('div', class_='article-info')
    vehicle_class = div.find(text=True, recursive=False).split('-')[0].strip() #type: ignore

    car = {
        'Name': name.text if name else None,
        'Class': vehicle_class if vehicle_class else None,
        'Top Speed': speed.text if speed else None,
        'Price': price.text if price else None
    }

#     print(car)

# name = soup.select_one("h3 a")
# price = soup.select_one("div.article-info span.field-value")
# speed = soup.select("div.article-info span.field-value")[1] # last one is usually speed
    
# print({
#         "name": name.text.strip() if name else None,
#         "price": price.text.strip() if price else None,
#         "speed": speed.text.strip() if speed else None
# })









