import requests
from bs4 import BeautifulSoup
url = "https://www.ghanaweb.com/"

response = requests.get(url)
if response.status_code == 200:
    print("Request was successful!")
    soup = BeautifulSoup(response.text, "html.parser")
    
    titles=soup.find_all("h3")

    for title in titles:
        print(title.get_text(strip=True))