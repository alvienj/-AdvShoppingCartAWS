from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium import webdriver
from time import sleep
import datetime
import sys

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def setUp():
    if driver is not None:
        print(f'Test started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')

    driver.maximize_window()

    driver.implicitly_wait(30)

    driver.get(locators.adshopcart_url)

    if driver.current_url == locators.adshopcart_url:
        print(f'We\'re at the Advantage Shopping homepage -- {driver.title}')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
    try:
        assert 'Advantage Shopping' in driver.title
        print(f'Title is good!')
    except Exception as e:
        print(f'Title is not matching, check code please')
    sleep(5)

def createnewaccount():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_adshopcart_username)
    sleep(2)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.adshopcart_email)
    sleep(2)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.adshopcart_password)
    sleep(2)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.adshopcart_password)
    sleep(2)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.adshopcart_firstname)
    sleep(2)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.adshopcart_lastname)
    sleep(2)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.adshopcart_phonenumber)
    sleep(2)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(2)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(2)

def myaccount():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(2)
    if driver.find_element(By.XPATH, "//*[@id='myAccountContainer']/div/div/div/label").is_displayed():
        print(f'The user with the name {locators.adshopcart_firstname} {locators.adshopcart_lastname} is displayed. Test passed.')
    sleep(2)


def shoppingcart():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My orders']").click()
    sleep(2)
    if driver.find_element(By.XPATH, "//*[contains(@class, 'bigEmptyOrder')]//*[contains(@class, 'roboto-bold')]").is_displayed():
        print(f'You currently do not have any orders!')
    sleep(2)

def signout():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='Sign out']").click()
    sleep(2)



def signin():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_adshopcart_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.adshopcart_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)

def deleteuser():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//div[text()='Delete Account']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//div[text()='yes']").click()
    sleep(10)

def checkifuserisdeleted():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_adshopcart_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.adshopcart_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    if driver.find_element(By.ID, 'signInResultMessage').is_displayed():
        print(f'You have successfully deleted the account.')
    sleep(2)
    driver.find_element(By.XPATH, "//*[contains(@class, 'closeBtn')]").click()
    sleep(2)

def displays():
    if driver.find_element(By.ID, 'speakersTxt').is_displayed:
        print(f'The SPEAKERS is displayed.')
    else:
        print(f'Not found. Please check your code.')
    sleep(2)
    if driver.find_element(By.ID, 'tabletsTxt').is_displayed:
        print(f'The TABLETS is displayed.')
    else:
        print(f'Not found. Please check your code.')
    sleep(2)
    if driver.find_element(By.ID, 'laptopsTxt').is_displayed:
        print(f'The LAPTOPS is displayed.')
    else:
        print(f'Not found. Please check your code.')
    sleep(2)
    if driver.find_element(By.ID, 'miceTxt').is_displayed:
        print(f'The MICE is displayed.')
    else:
        print(f'Not found. Please check your code.')
    sleep(2)
    if driver.find_element(By.ID, 'headphonesTxt').is_displayed:
        print(f'The HEADPHONES is displayed.')
    else:
        print(f'Not found. Please check your code.')

def tabs():
    driver.find_element(By.XPATH, "//a[text()='SPECIAL OFFER']").click()
    sleep(5)
    driver.find_element(By.XPATH, "//a[text()='POPULAR ITEMS']").click()
    sleep(5)
    driver.find_element(By.XPATH, "//a[text()='CONTACT US']").click()
    sleep(5)
    driver.find_element(By.XPATH, "//a[text()='OUR PRODUCTS']").click()
    sleep(5)
    if driver.find_element(By.XPATH, "//span[text()='dvantage']").is_displayed:
        print(f'We are at the home page.')
    sleep(2)

def contactus():
    Select(driver.find_element(By.XPATH, "//*[@name='categoryListboxContactUs']")).select_by_visible_text('Headphones')
    sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@name='productListboxContactUs']")).select_by_visible_text('HP H2310 In-ear Headset')
    sleep(2)
    driver.find_element(By.NAME, 'emailContactUs').send_keys('cool@gmail.com')
    sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys('Hello everyone!')
    sleep(2)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(2)


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'w')
    sys.stdout = log_file
    print(f'Username {locators.new_adshopcart_username} \nPassword: {locators.adshopcart_password}')
    sys.stdout = old_instance
    log_file.close()






