from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib

user=str(input("Enter VTOP User ID: "))
passwd=str(input("Enter VTOP Password: "))

#user="USERNAME_HERE"
#passwd="PASSWORD_HERE"

def BrowserSetup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=options)

def NavgiatePage():
    driver.get("https://vtop.vitbhopal.ac.in/vtop")
    loginToVTOPButton=driver.find_element("xpath","//*[@id='page-wrapper']/div/div[1]/div[1]/div[3]/div/button")
    loginToVTOPButton.click()
    time.sleep(0.5)
    
def FetchCaptcha():
    captchaImageElement=driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/form/div[3]/div/div/img")
    captchaSrc=captchaImageElement.get_attribute('src')
    urllib.request.urlretrieve(captchaSrc,"captcha.png")

def InputSignIn():
    import imgprocess
    driver.find_element(By.CSS_SELECTOR, "input[name='uname'][type='text']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[name='passwd'][type='password']").send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, "input[name='captchaCheck'][type='text']").send_keys(imgprocess.captchaAns)
    driver.find_element("xpath","//*[@id='captcha']").click()
    
BrowserSetup()
NavgiatePage()
FetchCaptcha()
InputSignIn()

input()
