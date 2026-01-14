# GTA Online Fastest lock-on Jammer vehicle

A Python script that scrapes a signle web page named GTA Online vehicles equipped with missile lock-on jammers from [GTABase](https://www.gtabase.com/), stores them in a sqlite DB, and identifies the top 10 fastest vehicles with a lock on jammer using Pandas.

---

## 📦 Features
- Scrapes GTABase's list for vehicles with a lock-on jammer
- Extracts and cleans data like vehicle name, vehicle class and top speed
- Stores results in a CSV file (`gtajammers.csv`)
- Finds the top 10 hicle with the highest top speed

---

## 🧰 Technologies Used
- **Python 3**
- **BeautifulSoup4** 
- **Requests**
- **Pandas**

---

## 🚀 Usage

```bash
# Clone this repo
git clone https://github.com/ThembaCal/no-lock-fastest.git

# Navigate into the project
cd no-lock-fastest

# Install dependencies
pip install -r requirements.txt

# Run the scraper
./script
