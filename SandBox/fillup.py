from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_link = "C://Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_link)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ifechukwu")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Ogidi")

mail = driver.find_element_by_name("email")
mail.send_keys("try@com.go")

sign = driver.find_element_by_tag_name("button")
sign.send_keys(Keys.ENTER)

driver.quit()