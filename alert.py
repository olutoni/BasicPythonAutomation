import time

from selenium import webdriver
validateText = "Options3"
driver = webdriver.Chrome(executable_path="C:\\selenium\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Options3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text

assert validateText in alertText
alert.accept()

driver.find_element_by_css_selector("#name").send_keys("Options3")
driver.find_element_by_id("confirmbtn").click()
alert_confirm = driver.switch_to.alert
alertText_confirm = alert_confirm.text
print(alertText_confirm)

time.sleep(5)
#Sassert validateText in alertText
#assert alert_confirm.dismiss()
try:
    alert_confirm.accept()
    print("confirm")
except:
    print("confirm didn't work")
    alert_confirm.dismiss()
    print("Confirmation was cancelled")