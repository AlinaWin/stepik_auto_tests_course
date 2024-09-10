from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x и выяисляем значение

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)

    # полученное значение вводим в инпут

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # выбираем чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # выбираем радиобаттон
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
