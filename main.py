import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# нажать на кнопку Visible After 5 Seconds
def press_button_visible_after_5_seconds():
    return driver_chrome.find_element(By.ID, "visibleAfter")


# базовый url
base_url = 'https://demoqa.com/dynamic-properties'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# обработка исключений
try:
    press_button_visible_after_5_seconds()
except NoSuchElementException:
    print("Получили ошибку 'NoSuchElementException'.")
    time.sleep(2)
    driver_chrome.refresh()
    time.sleep(5)
    press_button_visible_after_5_seconds()
    print("Нажатие на кнопку.")

# пауза
time.sleep(2)

# закрытие браузера
driver_chrome.quit()
print("Закрытие браузера.")
