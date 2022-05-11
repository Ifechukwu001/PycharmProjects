from selenium import webdriver

chrome_web_driver = "C://Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_web_driver)
driver.get("https://www.python.org/")

dates = driver.find_elements_by_css_selector(".event-widget time")
date_list = [date.text for date in dates]

titles = driver.find_elements_by_css_selector(".event-widget li a")
title_list = [title.text for title in titles]

events = {}
for _ in range(len(date_list)):
    events[_] = {"time": date_list[_], "name": title_list[_]}
print(events)


driver.quit()

