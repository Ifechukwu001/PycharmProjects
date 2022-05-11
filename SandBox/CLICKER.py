from selenium import webdriver
import time

chrome_link = "C://Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_link)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element_by_id("money")
cookie = driver.find_element_by_id("cookie")

cursor = driver.find_element_by_id("buyCursor")
grama = driver.find_element_by_id("buyGrandma")
factory = driver.find_element_by_id("buyFactory")
mine = driver.find_element_by_id("buyMine")
shipment = driver.find_element_by_id("buyShipment")
alchemy = driver.find_element_by_id("buyAlchemy lab")
portal = driver.find_element_by_id("buyPortal")
time_machine = driver.find_element_by_id("buyTime machine")

while True:
    cookie.click()


    time_machine.click()
    portal.click()
    alchemy.click()
    shipment.click()
    mine.click()
    factory.click()
    grama.click()
    cursor.click()


driver.quit()