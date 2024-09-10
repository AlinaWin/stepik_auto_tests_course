from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x и выяисляем значение

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # полученное значение вводим в инпут

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # выбираем чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # выбираем радиобаттон
    option1 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
