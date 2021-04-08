from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.firefox.options import Options

def checkRes():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.bseindia.com/corporates/ann.html")

    elem = Select(driver.find_element_by_id("ddlPeriod"))

    elem.select_by_visible_text("Result")

    elem = driver.find_element_by_id("btnSubmit")
    sleep(1)
    elem.click()
    elem.click()

    sleep(2)
    updSt = driver.find_element_by_xpath("//*[@id='fontSize']/div[2]/div[2]/div[1]/div[2]").text
    print(updSt)

checkRes()

