# задача на прикрепления файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем форму
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("rand@mail.com")

    # прикрепляем файл
    knopka = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(
        os.path.dirname(__file__)
    )  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(
        current_dir, "test.txt"
    )  # добавляем к этому пути имя файла
    knopka.send_keys(file_path)

    # жмем на кнопку сабмит
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
