from selenium import webdriver
import time
browser = webdriver.Chrome("C:\SE\chromedriver.exe")
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
time.sleep(2)
browser.maximize_window()
browser.get('http://139.162.35.76:8070/login')
time.sleep(2)
browser.find_element_by_name("email").send_keys("super@skylarksoft.com")
time.sleep(2)
browser.find_element_by_name("password").send_keys("Staging!Er$#P@2021")
time.sleep(2)
browser.find_element_by_name("login").click()
time.sleep(2)
browser.find_element_by_xpath("(//span[@class='nav-text'][contains(.,'Marketing')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("(//span[@class='nav-text'][contains(.,'Price Quotation')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("(//i[contains(@class,'fa fa-edit')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//button[contains(.,'Update')]").click()
time.sleep(2)
browser.find_element_by_xpath("//button[contains(.,'Costing Section')]").click()
time.sleep(4)
a = browser.find_element_by_xpath("//input[@name='embl_cost']")
action = ActionChains(browser)
action.double_click(a).perform()
time.sleep(3)
a1 = Select(browser.find_element_by_id("name"))
a1.select_by_index(1)
time.sleep(2)
a2 = Select(browser.find_element_by_id("type"))
a2.select_by_index(2)
time.sleep(2)
browser.find_element_by_xpath("//input[contains(@id,'cons_per_dzn')]").send_keys(".5")
time.sleep(3)
browser.find_element_by_xpath("//input[@id='rate']").send_keys("16")
time.sleep(3)
browser.find_element_by_xpath("//button[contains(.,'Add')]").click()
time.sleep(5)
browser.find_element_by_xpath("//span[contains(@id,'select2-name-container')]").click()
time.sleep(2)
browser.find_element_by_xpath("//li[contains(.,'Printing')]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(@id,'select2-type-container')]").click()
time.sleep(2)
browser.find_element_by_xpath("//li[contains(.,'Heat seal')]").click()
time.sleep(2)
browser.find_element_by_xpath("//button[contains(.,'Add')]").click()
time.sleep(5)
browser.find_element_by_xpath("//button[contains(.,'Save & Go Back')]").click()
time.sleep(3)