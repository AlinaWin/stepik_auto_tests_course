from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/cats.html"
browser.get(link)

 # жмем на кнопку
button = browser.find_element(By.ID, "button")
button.click()

