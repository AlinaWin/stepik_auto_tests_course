from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # жмем на кнопку
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    button.click()

    # переходим в новую вкладку, которая открылась рядом с текущей
    # browser.switch_to.window(browser.window_handles[1])
    next_window = browser.window_handles[1]
    browser.switch_to.window(next_window)

    # считаем выражение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # полученное значение вводим в инпут
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
