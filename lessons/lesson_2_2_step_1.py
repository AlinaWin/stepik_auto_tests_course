from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # найдем цифры и посчитаем их сумму

    x = browser.find_element(By.ID, "num1")
    a = int(x.text)

    y = browser.find_element(By.ID, "num2")
    b = int(y.text)

    sum = str(a + b)

    # раскроем список и найдем там значение, равное sum

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
