from selenium import webdriver


chrome_driver = "C://Development/chromedriver.exe"
EMAIL = "ogidiifechukwu6@gmail.com"
PASSWD = "CoderZ01"

driver = webdriver.Chrome(chrome_driver)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&keywords=python%20developer&sortBy=R")

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

email = driver.find_element_by_name("session_key")
email.send_keys(EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWD)
sign_button = driver.find_element_by_tag_name("button")
sign_button.click()