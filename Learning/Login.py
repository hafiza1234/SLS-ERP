from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome("C:\SE\chromedriver.exe")
mail = ['new@gmail.com','super@skylarksoft.com']
pw = ['2315651','Staging!Er$#P@2021']
time.sleep(2)
browser.maximize_window()
ab = len(mail)
print(ab)
browser.get('http://139.162.35.76:8070/login')
for x in range(ab):
    email = browser.find_element_by_xpath("//input[@id='email']")
    password = browser.find_element_by_xpath("//input[@id='password']")
    email.send_keys(mail[x])
    password.send_keys(pw[x])
    password.send_keys(Keys.ENTER)
    Login = browser.find_element_by_id("login")
    Login.click()
    print(mail[x])
    time.sleep(2)
    element = "new"
    assert element == 'new'
    print("wrong message")
    element1 = "Super"
    assert element1 == 'Super'
    print("Login successfully")


