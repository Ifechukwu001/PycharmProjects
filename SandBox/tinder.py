from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = "C://Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

driver.get("https://tinder.com")

time.sleep(15)
login = driver.find_element_by_xpath('//*[@id="q-184954025"]/div/div[1]/div/main/'
                                     'div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(10)
g_login = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
g_login.click()

time.sleep(15)
base_window = driver.window_handles[0]
g_login_window = driver.window_handles[1]
driver.switch_to.window(g_login_window)

email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys("techighbot@gmail.com")
e_next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
e_next.click()

time.sleep(10)
passwd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
passwd.send_keys("TecHIGHnet00")
p_next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
p_next.click()

driver.switch_to.window(base_window)

time.sleep(25)
allow_location = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

allow_cookies = driver.find_element_by_xpath('//*[@id="q-184954025"]/div/div[2]/div/div/div[1]/button')
allow_cookies.click()

allow_notification = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div/div/div[3]/button[2]')
allow_notification.click()

