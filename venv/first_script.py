import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser.get(link)
    time.sleep(1)
    browser.maximize_window()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    element = browser.switch_to.alert
    element.accept()
    time.sleep(1)
    x_element = browser.find_element(By.ID, 'input_value').text
    input_field = browser.find_element(By.ID, 'answer')
    result = calc(x_element)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input_field.send_keys(result)
    time.sleep(1)
    button.click()
    result_code = browser.switch_to.alert.text[-18:]
    time.sleep(5)
    browser.switch_to.alert.accept()
    russia_window = browser.window_handles[0]
    time.sleep(3)
    browser.switch_to.window(russia_window)
    # Запускаем второй скрипт с кодировкой utf-8 для того чтобы значения аттрибутов на русском языке отображались
    exec(open('course_script.py', 'r', encoding='utf-8').read())



except Exception as error:
    print(f'Error - {error}')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()
