import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element_by_id('autosuggest').send_keys('ind')
time.sleep(3)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == 'India':
        #country_value = country.text
        country.click()
        break
#print(country_value)
assert driver.find_element_by_id('autosuggest').get_attribute('value') == 'India'