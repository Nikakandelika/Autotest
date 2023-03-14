from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
icon = driver.find_element(By.CSS_SELECTOR, "header > a > img")
footer = driver.find_element(By.CSS_SELECTOR, "span")
button = driver.find_element(By.CSS_SELECTOR, "div > div > div.home-body > div > div")
s = [icon, footer, button]
for i in range(len(s)):
    if s[i] is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")