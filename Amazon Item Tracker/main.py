from bs4 import BeautifulSoup
import requests
import lxml
from pprint import pprint

link = "https://www.amazon.com/TRAVANDO-Wallet-Blocking-AUSTIN-Minimalist/dp/B07P73KK1J/"
title = "TRAVANDO Mens Slim Wallet with Money Clip AUSTIN RFID Blocking Bifold Credit Card Holder"
header= {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36",
    "accept-language": "en-US,en;q=0.7"

}
response = requests.get(link, headers=header, )
read = response.text

soup = BeautifulSoup(read, "html.parser")

# pprint(soup.prettify())

str_price = soup.select(selector="td span", class_="a-offscreen")[1].getText().strip(" ")
price = float(str_price[1:])

if price < 17.50:
    print(f"SALE!{title} is NOW selling for ${price}.")