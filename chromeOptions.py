from selenium import webdriver


# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

#chrome_options.binary_location= "C:\\Users\\oluto\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe', options=chrome_options)



driver.get('https://www.rahulshettyacademy.com/angularpractice/')

print(driver.title)
