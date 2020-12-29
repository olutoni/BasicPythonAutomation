import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

added_list = []
display_list = []
product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
driver = webdriver.Chrome(executable_path="C:\\selenium\chromedriver.exe")
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(4)
product_count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(product_count)
assert product_count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    added_list.append(button.find_element_by_xpath('parent::div/parent::div/h4').text)
    button.click()
print(added_list)

assert product_list == added_list

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# explict wait for the object
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'promoCode')))

veggies = driver.find_elements_by_css_selector('p.product-name')
for veg in veggies:
    display_list.append(veg.text)

print(display_list)

assert added_list == display_list

# if added_list == display_list:
#     print('list is same')

totalAmount = int(driver.find_element_by_css_selector('.totAmt').text)
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_css_selector('.promoBtn').click()

wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.promoInfo')))
discountAmount = driver.find_element_by_css_selector('.discountAmt').text

assert float(discountAmount) < int(totalAmount)


print(driver.find_element_by_css_selector('span.promoInfo').text)

#locate individual amounts for each product
amounts = driver.find_elements_by_xpath('//tr/td[5]/p')

amountSum = 0

for amount in amounts:
    amountSum = amountSum + int(amount.text)

print(amountSum)
print(totalAmount)
print(discountAmount)

assert amountSum == totalAmount

