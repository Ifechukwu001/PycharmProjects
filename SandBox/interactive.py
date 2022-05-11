from selenium import webdriver

chrome_web_driver = "C://Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_web_driver)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

links = driver.find_element_by_css_selector("#articlecount a").text

print(links)

driver.quit()