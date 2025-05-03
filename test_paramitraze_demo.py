from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


users = ['user1@mail.com', 'user2@mail.com']
passws = ['asasasa', 'qwqwqwqw']

def generate_pairs():
    pairs = []
    for user in users:
        for passw in passws:
            pairs.append(pytest.param((user, passw), id = user))
    return pairs


# @pytest.mark.parametrize('creds', [pytest.param(('user1@mail.com', 'asasasas'), id='user1@mail.com, asasasas'),
#                                    pytest.param(('user2@mail.com', 'aqwwqwqw'), id='user2@mail.com, aqwwqwqw'),
#                                    pytest.param(('user3@mail.com', 'azxzxzxz'), id='ser3@mail.com, azxzxzxz')])
@pytest.mark.skip
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, passw = creds
    driver = webdriver.Firefox()
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'send2').click()
    sleep(3)
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    error_text_true = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    sleep(1)
    driver.quit()
    assert (error_text_true == error_text)


@pytest.fixture()
def page(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'wats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    yield driver
    driver.quit()

@pytest.mark.parametrize('page', ['wats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1').text
    assert title == "What's New"

@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1').text
    assert title == "Sale"