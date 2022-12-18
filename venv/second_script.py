from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import calc

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    #Ждем до момента когда текст в элементе будет равен "$100"
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    x_element = browser.find_element(By.ID, 'input_value').text
    input_field = browser.find_element(By.ID, 'answer')
    result = calc(x_element)
    input_field.send_keys(result)
    button1 = browser.find_element(By.ID,'solve')
    button1.click()



except Exception as error:
    print(f'ошибка: {error}')


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
