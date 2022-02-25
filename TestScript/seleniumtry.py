from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "/Users/turanmertduran/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:5500/CS458_Netfilix_Sign_In/Index.html")

signInBtn = driver.find_element_by_id("signIn")
emailF = driver.find_element_by_id("email")
passwordF = driver.find_element_by_id("password")
signInBtn.click()

emailF.send_keys("radman@gmail.com")
passwordF.send_keys("123456")
signInBtn.click()

#driver.find_element("email")
#driver.find_element("password")