from selenium import webdriver

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.get('https://login.salesforce.com/')

driver.find_element_by_css_selector("#username").send_keys("neyochi")
driver.find_element_by_css_selector(".password").send_keys("viper")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
#//tagname[contains(text(), ‘actual-text’)]
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
#print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)").text)

