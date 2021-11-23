from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
contact = "Cnh"
text = "this is a message sent automatically. finally done by nicole at 0100 23 Nov 2021!!!!!"
driver = webdriver.Chrome('/Users/nicolechui/Downloads/chromedriver')
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
# inp_xpath_search = "//input[@title='Search or start new chat']"
# input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
# input_box_search.click()
time.sleep(2)
# input_box_search.send_keys(contact)
# time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='{}']".format(contact))
# selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
# time.sleep(2)
# inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
# input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)

msg_box = driver.find_element_by_class_name('p3_M1')
msg_box.send_keys(text + Keys.ENTER)
# button = driver.find_element_by_class_name('_1UWac _1LbR4')
# button.click()
# # selected_contact.send_keys(text + Keys.ENTER)
time.sleep(2)
driver.quit()
