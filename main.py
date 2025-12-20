import requests 
from os.path import exists
import pandas as pd
import sqlite3
# from db import create_db
from bs4 import BeautifulSoup


def get_page(url: str) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def parse_page(page) -> BeautifulSoup:
    return BeautifulSoup(page, 'lxml') 


def extract_data(soup: BeautifulSoup) -> list:
    car_content = soup.select('div.item-info')
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
            'Vehicle Name': name.text.strip() if name else None,
            'Vehicle Class': vehicle_class,
            'Top Speed (mph)': values[1].text.strip()  if len(values) > 1 else None,
            'Price ($)': values[0].text.strip()  if len(values) > 0  else None,
        }

        data.append(car_info)

    return data
     

def clean_data(data: list) -> pd.DataFrame:
    df  = pd.DataFrame(data)
    df = df.dropna()
    
    df['Price ($)'] = df['Price ($)'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    df['Price ($)'] = df['Price ($)'].astype(float).round(2)
    
    df['Top Speed (mph)'] = df['Top Speed (mph)'].str.split(' ').str[0]
    df['Top Speed (mph)'] = df['Top Speed (mph)'].astype(float).round(2)
    
    df.sort_values(by=['Vehicle Class', 'Vehicle Name'], ascending=True, inplace=True)
    df.reset_index(drop=True,inplace=True)
    return df

def save_csv(df: pd.DataFrame):
    file_name = 'gta_jammers'
    num = 0
    if exists(file_name):
        num += 1
        df.to_csv(f"data/{file_name}{num:.2f}.csv", index=False)
    else:
        df.to_csv("data/gta_jammers.csv")



def results_gen(df: pd.DataFrame):
    results = df.sort_values(by='Top Speed (mph)', ascending=False)
    print(results.head(10).to_markdown(floatfmt='.2f'))


def main():
    url = "https://www.gtabase.com/grand-theft-auto-v/guides/list-of-vehicles-in-gta-5-gta-online-by-feature?feature=missile-lockon-jammer"
    html = get_page(url)
    soup = parse_page(html)
    data = extract_data(soup)
    df = clean_data(data)
    # save_csv(df)
    conn = sqlite3.connect("data/cars.sqlite")
    df.to_sql(name='cars', con=conn, if_exists='replace', index=False)
    results_gen(df)


if __name__ == "__main__":
    main()