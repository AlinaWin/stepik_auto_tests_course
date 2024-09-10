from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #жмем на кнопку
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    #в confirm окне жмем Ок
    confirm = browser.switch_to.alert
    confirm.accept()

    #считаем выражение 
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

     #полученное значение вводим в инпут
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
