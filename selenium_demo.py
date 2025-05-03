from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://9gag.com/trending')
first_meme = driver.find_element(By.CLASS_NAME, 'badge-evt')
first_meme_url = first_meme.get_attribute('href')
driver.close()
with open('meme.txt', 'w') as meme_file:
    meme_file.write(first_meme_url)