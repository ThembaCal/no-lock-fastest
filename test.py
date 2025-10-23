# from bs4 import BeautifulSoup
import sqlite3

# with open('testfile.txt', 'r') as file:
#     line = file.readlines()
#     # lists = line.split()
#     # print(line)
#     # print(type(line))

# file = open('index.html', 'r')

# soup = BeautifulSoup(file, 'lxml')

# car_content = soup.select('div.item-info')

# print(car_content)

# for car in car_content:
#     name = car.select_one('span.badge')
#     tag = car.find("span")
#     speed = car.select('span.field-value')[1]
#     price = car.select('span.field-value')[0]
#     div = car.find('div', class_='article-info')
#     vehicle_class = div.find(text=True, recursive=False).split('-')[0].strip() #type: ignore

#     car = {
#         'Name': name.text if name else None,
#         'Class': vehicle_class if vehicle_class else None,
#         'Top Speed': speed.text if speed else None,
#         'Price': price.text if price else None
#     }

#     print(car)

# name = soup.select_one("h3 a")
# price = soup.select_one("div.article-info span.field-value")
# speed = soup.select("div.article-info span.field-value")[1] # last one is usually speed
    
# print({
#         "name": name.text.strip() if name else None,
#         "price": price.text.strip() if price else None,
#         "speed": speed.text.strip() if speed else None
# })

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)") #creates an error because DB already exits

# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

# print(res.fetchone() is None)

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

# con.commit()

# res = cur.execute("SELECT score FROM movie")

# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.

# print(res.fetchall())


for row in cur.execute("SELECT year, title FROM movie"):

    print(row)









