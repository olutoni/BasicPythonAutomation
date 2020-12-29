from selenium import webdriver

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
#driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
#driver = webdriver.Firefox(executable_path="C:\\selenium\geckodriver.exe")
driver = webdriver.Edge(executable_path="C:\\selenium\\msedgedriver.exe")
driver.maximize_window()
driver.get('https://www.rahulshettyacademy.com/#/index')


print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
