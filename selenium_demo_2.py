from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.qa-practice.com/elements/button/simple')
click_button = driver.find_element(By.ID, 'submit-id-submit')
sleep(3)
click_button.click()
driver.find_element(By.LINK_TEXT, 'Contact').click()

#css_selector
driver.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]').click()

#xpath
driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()
#driver.close()