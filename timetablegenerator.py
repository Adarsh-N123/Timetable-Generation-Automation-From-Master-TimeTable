#import webdriver
import os
from selenium import webdriver

import pdfkit
import chromedriver_binary
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
zoom_level = 0.3
#import By method to find the elements
from selenium.webdriver.common.by import By
#import time library to give sleep time to load data(bcz if we try to extract the data before getting loaded then we may get errros)
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager
#basically selenium uses a bot for automation and it opens a browser window when run the code so to remove the window we have to import and set options
from selenium.webdriver.firefox.options import Options
from PIL import Image

from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
import json
#importing requests
import requests
#importing beautifulsoup for scraping
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service 
#from webdriver_manager.firefox import GeckoDriverManager
#geckodriver_path = './geckodriver.exe'
# webdriver.gecko.driver = geckodriver_path
# service = Service(ChromeDriverManager().install())
firefox_options = Options()
firefox_options.add_argument("--zoom={:.2f}".format(zoom_level))
#firefox_options.binary_location = os.environ["PATHCHROME"]
#firefox_options.binary_location = './firefox/firefox'
import os
#os.chmod('./firefox/firefox', 0o755)
# firefox_options.binary_location = geckodriver_path
#setting the --headless argument to stop the browser window from opening as selenium is a type of automated browser software it opens browser window when we run code
# firefox_options.add_argument("--headless")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.add_argument('--disable-web-security')
firefox_options.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=firefox_options)
# driver = webdriver.Chrome(options=firefox_options)
url = "C:\\Users\\dell\\Desktop\\timetable\\ttfinal.html"
driver.get(url)
w = driver.execute_script('return document.body.parentNode.scrollWidth')
h = driver.execute_script('return document.body.parentNode.scrollHeight')
#set to new window size
driver.set_window_size(w, 3*h)
elements = driver.find_elements(By.XPATH,"//td")
count=0
for i in elements:
    # print(count)
    # print(i.get_attribute("innerHTML"))
    count+=1
    if count>2000:
        break
    driver.execute_script("""
        var data = String(arguments[0].innerHTML);
        
        function containsSubstring(string, substrings) {
            var stringdata = "";
            if (string.includes("0-0")||string.includes("0-1")){
                          return string;
            }
            for (let i = 0; i < substrings.length; i++) {
                if (string.includes(substrings[i])) {
                    stringdata = stringdata+","+substrings[i];
                    
                }
            }
            return stringdata.substring(1);
        }
        
        arguments[0].innerHTML = containsSubstring(data,["CS300","CS310","CS320","CS330","CS572","Monday","Tuesday","Wednesday","Thursday","Friday","LH1","LT1  - 84","LT2  - 73","LT3  - 70","LT4  - 72","CL2  - 35","CL3  - 35","T1    - 24 ","T2    - 24 ","T3    - 24 ","Lab","TIMETABLE FOR AUTUMN SEMESTER OF AY 2023-24"])
    """,i)
    i.get_attribute("innerHTML")

# time.sleep(100)
driver.save_screenshot("cstt.png")
screenshot = Image.open("cstt.png")
width, height = screenshot.size

# Crop the right half of the screenshot
cropped_screenshot = screenshot.crop((0, 0, width, height//5))
cropped_screenshot_path = 'cstt.png'
cropped_screenshot.save(cropped_screenshot_path)
# pdfkit.from_string(driver.page_source, 'output.pdf')
driver.quit()