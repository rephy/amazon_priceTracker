import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Texas-Instruments-Calculator-Certified-Refurbished/dp/B07HG3WGVY/ref=sr_1_5?crid=1ZF5CSK6YN5MN&dib=eyJ2IjoiMSJ9.TWJeX2tZXfhY2G23qRid3MxzrcCbjTpNq1EuXVJJO-wpQovXhnMULy6sbcyNsPgXC0szT9QUOe2TZdEikbFQVjl6xpRrWG4vkluklnkriBcUyb5dSP8QCpSrOmFDDcD5H0e5DdjwDQBB_qMMuXQe4Vfs7adXCYKzse6rInN9yVu4ClN_fc1YbLCqgBzd-bQGF6lzz2oZtfyQgDL4XSi-2jYvo5CqRbI3YyUKA-8euiE.eTI8ZWJyc8Z8W9vOE3KEs8hA5O1xcolvKg026PIZfq8&dib_tag=se&keywords=ti-84&qid=1718416133&sprefix=ti-84%2Caps%2C203&sr=8-5" # Replace with URL of your desired Amazon product
good_price = 100 # Any deal given to you is below this price in USD

website = requests.get(url=URL).text

soup = BeautifulSoup(website, "html.parser")
price = float(soup.select_one("td span.a-offscreen").getText()[1:]) # in USD
print(price)

if price <= good_price:
    print("Good deal!")