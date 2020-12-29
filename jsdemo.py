from selenium import webdriver


# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name('name').send_keys('hello')
#using selenium
print(driver.find_element_by_name('name').get_attribute('value'))
#using JS executor
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector('a[href*= "shop"]')
driver.execute_script("arguments[0].click();", shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
