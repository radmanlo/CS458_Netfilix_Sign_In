from _ast import Assert
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

chromeDriver = webdriver.Chrome("/Users/turanmertduran/Desktop/chromedriver")
geckoDriver = webdriver.Firefox(executable_path="/Users/turanmertduran/Desktop/geckodriver")
def sucSignInTry(driver):
    driver.get("http://localhost:5500/CS458_Netfilix_Sign_In/Index.html")
    signInBtn = driver.find_element_by_id("signIn")
    emailF = driver.find_element_by_id("email")
    passwordF = driver.find_element_by_id("password")

    emailF.send_keys("radman@gmail.com")
    passwordF.send_keys("123456")
    signInBtn.click()

    time.sleep(3)

    page_title = driver.title
    assert page_title == "Main"

#sucSignInTry(geckoDriver)
#sucSignInTry(chromeDriver)

def unSucSignInTry(driver):
    driver.get("http://localhost:5500/CS458_Netfilix_Sign_In/Index.html")
    signInBtn = driver.find_element_by_id("signIn")
    emailF = driver.find_element_by_id("email")
    passwordF = driver.find_element_by_id("password")

    emailF.send_keys("radman.com")
    passwordF.send_keys("123456")
    signInBtn.click()

    time.sleep(3)
    driver.switch_to.alert.accept()
    page_title = driver.title
    assert page_title == "Netflix"

#unSucSignInTry(geckoDriver)
#unSucSignInTry(chromeDriver)

def keyboardNavigationTest(driver):
    driver.get("http://localhost:5500/CS458_Netfilix_Sign_In/Index.html")
    element = driver.switch_to.active_element
    if driver == chromeDriver:
        element.send_keys(Keys.TAB)

    element.send_keys(Keys.TAB)
    element = driver.switch_to.active_element
    element.send_keys("radman@gmail.com")
    element.send_keys(Keys.TAB)
    element = driver.switch_to.active_element
    element.send_keys("123456")
    element.send_keys(Keys.TAB)
    element = driver.switch_to.active_element
    element.send_keys(Keys.ENTER)
    time.sleep(3)
    page_title = driver.title
    assert page_title == "Main"

#keyboardNavigationTest(geckoDriver)
#keyboardNavigationTest(chromeDriver)
#geckoDriver.close()
#chromeDriver.close()