from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import time
import urllib
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(options=options)
driver.get("https://vtop.vitbhopal.ac.in/vtop")

loginToVTOPButton=driver.find_element("xpath","//*[@id='page-wrapper']/div/div[1]/div[1]/div[3]/div/button")
loginToVTOPButton.click()

user="USERNAME_HERE"
passwd="PASSWORD_HERE"
time.sleep(0.5)
usernamefield=driver.find_element(By.CSS_SELECTOR, "input[name='uname'][type='text']")
passwordfield=driver.find_element(By.CSS_SELECTOR, "input[name='passwd'][type='password']")
usernamefield.send_keys(user)
passwordfield.send_keys(passwd)
captchaImageElement=driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/form/div[3]/div/div/img")
captchaSrc=captchaImageElement.get_attribute('src')
urllib.request.urlretrieve(captchaSrc,"captcha.png")
cropped_image=Image.open("captcha.png").convert("L")
pixel_matrix = cropped_image.load()
for col in range(0, cropped_image.height):
    for row in range(0, cropped_image.width):
        if pixel_matrix[row, col] != 0:
            pixel_matrix[row, col] = 255
cropped_image.save("captcha_clean.png")
import imgprocess
captchafield=driver.find_element(By.CSS_SELECTOR, "input[name='captchaCheck'][type='text']")
captchafield.send_keys(imgprocess.captchaAns)
signinButton=driver.find_element("xpath","//*[@id='captcha']")
signinButton.click()