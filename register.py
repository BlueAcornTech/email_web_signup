from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
CHROME_DRIVER = '/Users/child/Desktop/001 - WMDs/driver/chromedriver'
store_email = ["wtfbrahh@gmail.com", "businessinquiries@thecollective-la.com"]
email = "22tipirneni@lexingtonma.org"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=options)
file = open('webs.txt', 'r')
webs = file.readlines()
file.close()
for i in range(0,len(webs), 3):
    time.sleep(0.5)
    url = webs[i]
    print(url)
    driver.get(url)
    if int(webs[i+2]) == 1:
        try:
            elem = driver.find_element_by_name(webs[i+1].rstrip())
            elem.send_keys(email)
            elem.send_keys(Keys.ENTER)
        except Exception as e:
            print("Error")
    if int(webs[i+2]) == 2:
        try:
            elem = driver.find_element_by_id(webs[i+1].rstrip())
            elem.send_keys(email)
            elem.send_keys(Keys.ENTER)
        except Exception as e:
            print(str(e))
driver.close()
        
    
