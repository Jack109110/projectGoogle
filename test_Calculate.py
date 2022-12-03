import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_calculate():
    s = Service('C:/chromedriver2.exe')
    driver = webdriver.Chrome(service=s)

    driver.get('https://www.google.ru/')

    element = driver.find_element(By.NAME, 'q')

    element.send_keys('калькулятор')

    element.send_keys(Keys.ENTER)

    element2 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
    element2.click()
    element3 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
    element3.click()
    element4 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
    element4.click()
    element5 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
    element5.click()
    element6 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
    element6.click()
    element7 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
    element7.click()
    element8 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
    element8.click()
    element9 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')
    element9.click()

    time.sleep(2)

    element10 = driver.find_element(By.XPATH, '//*[@id="cwos"]')
    assert (element10, 0)

    driver.quit()
