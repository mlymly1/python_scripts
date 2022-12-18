
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from first_script import result_code
from auth_data import Password, Login


link2 = 'https://stepik.org/lesson/184253/step/4'
try:
    browser.get(link2)
    time.sleep(5)
    entrance_button = browser.find_element(By.CSS_SELECTOR, '[href = "/course/575/promo?auth=login"]')
    entrance_button.click()
    email_input = browser.find_element(By.ID, 'id_login_email')
    password_input = browser.find_element(By.ID, 'id_login_password')
    email_input.send_keys(Login)
    password_input.send_keys(Password)
    entry = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    entry.click()
    time.sleep(2)
    browser.get(link2)
    #reset_button = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
    #reset_button.click()
    text_area = browser.find_element(By.CSS_SELECTOR,'[placeholder = "Напишите ваш ответ здесь..."]')
    text_area.send_keys(result_code)
    send_button = browser.find_element(By.CSS_SELECTOR,'button.submit-submission')
    send_button.click(123)
    send_button.click






except Exception as error:
    print(f'Error: {error}')


finally:
    time.sleep(5)
    browser.quit()
print(123123)