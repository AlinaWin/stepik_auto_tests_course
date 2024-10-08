from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book")
button.click()

# считаем выражение
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

# полученное значение вводим в инпут
input = browser.find_element(By.ID, "answer")
input.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
