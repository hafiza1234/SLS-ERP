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
browser.find_element_by_xpath("(//span[contains(.,'General Settings')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(.,'Assign Permission')]").click()
time.sleep(2)
browser.find_element_by_xpath("//a[@href='http://139.162.35.76:8070/assign-permissions/create']").click()
time.sleep(2)
a1 = Select(browser.find_element_by_id("assign_permission_factory_id"))
a1.select_by_index(1)
time.sleep(3)
a2 = Select(browser.find_element_by_name("user_id[]"))
a2.select_by_index(5)
time.sleep(3)
a3 = Select(browser.find_element_by_name("module_ids[]"))
a3.select_by_index(10)
time.sleep(3)
browser.find_element_by_xpath("(//button[@type='button'])[1]").click()
time.sleep(3)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
browser.find_element_by_xpath("(//button[contains(@type,'submit')])[2]").click()
time.sleep(3)