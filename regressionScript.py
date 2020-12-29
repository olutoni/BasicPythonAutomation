from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\selenium\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

shopButton = driver.find_element_by_css_selector('a[href*= "shop"]')
shopButton.click()

products = driver.find_elements_by_xpath('//div[@class="card h-100"]')
for product in products:
    productName = product.find_element_by_xpath('div[1]/h4/a').text
    # print(product.find_element_by_xpath('div[1]/h4').text)
    if productName == 'Blackberry':
        # find add button
        addButton = product.find_element_by_xpath('div[2]/button')
        # add item to cart
        addButton.click()

driver.find_element_by_class_name('btn-primary').click()

driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_id('country').send_keys('uni')
wait = WebDriverWait(driver, 8)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li")))
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'United States of America')))
# wait.until(expected_conditions.presence_of_all_elements_located(
#     (By.XPATH, "//div[@class='suggestions']/ul/li/a")))
print(driver.find_element_by_link_text('United States of America').text)
countries = driver.find_elements_by_xpath(
    "//div[@class='suggestions']/ul/li/a")
print(len(countries))
for country in countries:
    if country.text == 'United States of America':
        country_value = country.text
        print(country_value)
        country.click()
        break
assert driver.find_element_by_id('country').get_attribute(
    'value') == 'United States of America'
# "//div[@class='suggestions']/ul/li/a"
driver.find_element_by_xpath(
    "//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector('[type="submit"]').click()

successMessage = driver.find_element_by_class_name('alert-success').text

assert 'Success! Thank you!' in successMessage

driver.get_screenshot_as_file("screen.png")
