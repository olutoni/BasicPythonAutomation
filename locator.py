

from selenium import webdriver

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver = webdriver.Firefox(executable_path='C:\\selenium\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

#driver.find_element_by_name("name").send_keys("Adeniyi")


driver.find_element_by_css_selector("input[name='name']").send_keys("nyc")
driver.find_element_by_name("email").send_keys("yoyo")
driver.find_element_by_id("exampleInputPassword1").send_keys("viper")
driver.find_element_by_id("exampleCheck1").click()


dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()
driver.find_element_by_xpath("//input[@type='submit']").click()

#print(driver.find_element_by_class_name("alert-success").text)

message = driver.find_element_by_class_name("alert-success").text
assert "success" in message





