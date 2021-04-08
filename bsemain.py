from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.firefox.options import Options
import ctypes
import winsound

def Mbox(msg):
    return ctypes.windll.user32.MessageBoxW(None, msg, 'ALERT!!', 0x1000)


print("Script Started! You will get a pop up with sound when BSE result page is updated!")

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.bseindia.com/corporates/ann.html")
elem = Select(driver.find_element_by_id("ddlPeriod"))
elem.select_by_visible_text("Result")
elem = driver.find_element_by_id("btnSubmit")
sleep(5)
elem.click()
elem.click()
sleep(2)
updSt1 = driver.find_element_by_xpath("//*[@id='fontSize']/div[2]/div[2]/div[1]/div[2]").text
dwn = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[1]/tbody/tr[1]/td[3]/a/i")
dwn.click()

while(1):
    elem = driver.find_element_by_id("btnSubmit")
    elem.click()
    elem.click()
    sleep(2)
    updSt2 = driver.find_element_by_xpath("//*[@id='fontSize']/div[2]/div[2]/div[1]/div[2]").text
    if(updSt1==updSt2):
        continue
    else:
        winsound.PlaySound("SystemAsterisk",winsound.SND_ALIAS)
        Mbox('New Result Available!!')
        updSt1=updSt2
        dwn = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[1]/tbody/tr[1]/td[3]/a/i")
        dwn.click()
    

