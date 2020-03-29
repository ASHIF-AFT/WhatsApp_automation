from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



browser=webdriver.Chrome("E:/pcsw/chromedriver")#THIS is the path for chrome webdriver,for diiferent browser
#different web driver are available
browser.get("https:/web.whatsapp.com/")
wait=WebDriverWait(browser,600)
target='"name of your friend"' #just type your friend name in your whatsapp contact
string="msg goes here"#the message which you want to send repeatedly
x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box=browser.find_element_by_class_name('_1Plpp')#this is the class name of your friend's message box,by inspecting we can get that
for i in range(10000):
    input_box.send_keys(string+Keys.ENTER)#automating enter button after typing the message
    if i%1000==0:
        time.sleep(2)