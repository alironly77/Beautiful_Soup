import requests
from bs4 import BeautifulSoup


page = requests.get(
    "https://www.mex.co.ir/")  # Request URL

soup = BeautifulSoup(page.content, "html.parser")  # Fetch webpage
price_dollar = soup.find(
    "td", text="USD").find_next("td").text  # Scraping Data

Convert_to_Toman = int(input("Price in Tomans:"))
price_dollar = price_dollar[0:2]
The_final_price = Convert_to_Toman/int(price_dollar)
print(The_final_price)
