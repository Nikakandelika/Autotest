from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.CSS_SELECTOR, "#user-name")
password = driver.find_element(By.CSS_SELECTOR, "#password")
submit = driver.find_element(By.CSS_SELECTOR, "#login-button")
list = [username, password, submit]
for i in range(len(list)):
    if list[i] is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")