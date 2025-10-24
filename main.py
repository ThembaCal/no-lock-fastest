import requests 
from bs4 import BeautifulSoup
import pandas as pd


''' SCRAPE '''

url = "https://www.gtabase.com/grand-theft-auto-v/guides/list-of-vehicles-in-gta-5-gta-online-by-feature?feature=missile-lockon-jammer"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'lxml') 

''' EXTRACT '''

car_content = soup.select('div.item-info')

''' ORGANIZE '''

data = []

for car in car_content:
    name = car.select_one('h3')
    tag = car.find("span")

    values = car.select('span.field-value')
    div = car.find('div', class_='article-info')
    try:
        vehicle_class = div.find(string=True, recursive=False).split('-')[0].strip() #type: ignore
    except AttributeError:
        vehicle_class = None

    car_info = {
        'Name': name.text.strip() if name else None,
        'Vehicle Class': vehicle_class,
        'Top Speed': values[1].text.strip()  if len(values) > 1 else None,
        'Price': values[0].text.strip()  if len(values) > 0  else None,
    }

    data.append(car_info)


# fieldnames = list(data[0].keys())

# with open('output.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)



''' CLEAN '''

raw_data  = pd.DataFrame(data)

df = raw_data.dropna()

df['Price'] = df['Price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['Price'] = df['Price'].astype(float).round(2)

df['Top Speed'] = df['Top Speed'].str.split(' ').str[0]
df['Top Speed'] = df['Top Speed'].astype(float).round(2)

# df['Class'] = df['Class'].sort

df.rename(columns={
    'Price': 'Price ($)',
    'Name': 'Vehicle Name',
    'Top Speed': 'Top Speed (mph)',
    'Class': 'Vehicle Class',
}, inplace=True)

df.sort_values(by=['Vehicle Class', 'Vehicle Name'], ascending=True, inplace=True)
df.reset_index(drop=True,inplace=True)


''' STORE '''
df.to_csv('gta_jammers.csv', index=False)


''' RESULTS '''
results = df.sort_values(by='Top Speed (mph)', ascending=False)
# print(df.to_markdown(floatfmt='.2f'))
print(results.head(10).to_markdown(floatfmt='.2f'))
