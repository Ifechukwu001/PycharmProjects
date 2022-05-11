import smtplib
from bs4 import BeautifulSoup
import requests

BUY_PRICE = 400
my_email = "techighbot@gmail.com"
password = "TecHIGHnet00"
url = "https://www.amazon.com/ASUS-i3-1005G1-Processor-Fingerprint-F515JA-AH31/dp/B0869L1326/ref=sr_1_6?" \
      "qid=1638538066&refinements=p_89%3AASUS&rnid=2528832011&s=computers-intl-ship&sr=1-6&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=url, headers=headers)
# response.raise_for_status()
amazon_content = response.text

soup = BeautifulSoup(amazon_content, "html.parser")
product_price = float(soup.select(selector=".apexPriceToPay .a-offscreen")[0].string.strip("$"))

if product_price < 400:
    title = "Buy Your Laptop Now"
    message = f"The price of the laptop ASUS-i3 is currently at {product_price}. Buy it here.{url}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ogidiifechukwu4@gmail.com",
            msg=f"Subject:{title}\n\nHi, {message}"
        )
        