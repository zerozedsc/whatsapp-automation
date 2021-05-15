from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from tkinter import filedialog
import os
import random

media_dir = filedialog.askdirectory()
print(media_dir)

#PHONE NUMBER
with open("phonenumber.txt" , "r") as read:
    list_phone = [k.strip("\n") for k in read.readlines()]
    read.close()
print(list_phone)

#WORD
with open("spamword.txt", "r", encoding="utf8") as word:
    list_word = [a.strip("\n") for a in word.readlines()]
    word.close()

#MEDIA
media_path = []
for path in os.listdir(media_dir):
    full_path = os.path.join(media_dir, path)
    if os.path.isfile(full_path):
        media_path.append(full_path)

driver = webdriver.Chrome('chromedriver90.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

check_login = True
delay = 5
while check_login:
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_27MZN'))) #check already log in or not
        print("Page is ready! >>", myElem)
        check_login = False

    except Exception as e:
        print(f"Loading took too much time!, {e}")
        check_login = True
        delay+=2

if not check_login:
    print("SUCCESSFULLY LOGIN")
    #TESTING

    for i in list_phone:
        try:
            href = f"https://web.whatsapp.com/send?phone={i}" + "&text&app_absent=0"
            driver.get(href)
            time.sleep(10)
            for media in media_path:
                driver.find_element_by_css_selector("span[data-icon='clip']").click()
                time.sleep(2)
                print(media)
                driver.find_element_by_css_selector("input[type='file']").send_keys(media)
                time.sleep(1)
                send_button = driver.find_element_by_class_name('_3v5V7')
                send_button.click()
                time.sleep(2)
                txt_msg = str(random.choice(list_word))
                txt_box = driver.find_element_by_class_name('_2A8P4').send_keys(txt_msg + Keys.ENTER)
                time.sleep(1)
        except Exception as e:
            print(f"{i} >> {e}")

driver.close()

