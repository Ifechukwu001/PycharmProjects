import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Accept-Language": "en-US,en;q=0.5"
}
form = "https://docs.google.com/forms/d/e/1FAIpQLSff8rXJ94TLTzDVppW-Z6SEOkphcYmnujiOPV6-4zZLNev6iw/viewform?usp=sf_link"

zillow = requests.get(url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B"
                          "%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.91045397224796%2C%22east%22%3A-121"
                          ".95876329841984%2C%22south%22%3A37.50868742551738%2C%22north%22%3A38.040571058049366%7D%2C"
                          "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D"
                          "%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A"
                          "%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22"
                          "%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D"
                          "%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C"
                          "%22isListVisible%22%3Atrue%7D", headers=headers)

zillow_content = BeautifulSoup(zillow.content, "html.parser")

addresses= zillow_content.select(selector=".list-card-addr")
address_list =[address.text for address in addresses]

prices = zillow_content.select(selector=".list-card-price")
price_list = [price.text[:6] for price in prices]

links = zillow_content.select(selector=".list-card-info .list-card-link")
link_list = [link.get("href") if "https://www.zillow.com" in f"{link.get('href')}"
             else f"https://www.zillow.com{link.get('href')}"for link in links]

for index in range(len(address_list)):
    driver = webdriver.Chrome("C:/Development/chromedriver.exe")

    driver.get(form)

    time.sleep(10)

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    address.send_keys(address_list[index])

    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                         '1]/div/div[1]/input')
    price.send_keys(price_list[index])

    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                        '1]/div/div[1]/input')
    link.send_keys(link_list[index])

    submit = driver.find_element_by_class_name("exportButtonContent")
    submit.click()

    driver.quit()



