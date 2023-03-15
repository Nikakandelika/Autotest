def page(a, b, c):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_elements(By.CSS_SELECTOR, a)
    password = driver.find_elements(By.CSS_SELECTOR, b)
    submit = driver.find_elements(By.CSS_SELECTOR, c)
    list = [a, b, c]
    for i in range(len(list)):
        if list[i] is None:
            return "Элемент не найден"
        else:
            return "Элемент найден"

print(page("user-name", "password", "login-button"))