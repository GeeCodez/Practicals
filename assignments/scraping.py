import requests
from bs4 import BeautifulSoup

url = "https://www.ghpage.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.select("h3 a")

    for headline in headlines:
        print(headline.get_text(strip=True))