import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(4)
product_count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(product_count)
assert product_count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_css_selector('.promoBtn').click()
print(driver.find_element_by_css_selector('span.promoInfo').text)