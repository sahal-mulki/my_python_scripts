from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

__author__ = "Sahal Mulki"

print("Made by Sahal Mulki")
options = Options()
options.headless = True
cap = DesiredCapabilities().FIREFOX

driver = webdriver.Firefox(options=options, capabilities=cap, executable_path=r"C:\Users\M.Sahal\Desktop\geckodriver.exe")
driver.get("https://time.is/just")

time = driver.find_element_by_id('time_section')
print(time.text)

driver.quit()
