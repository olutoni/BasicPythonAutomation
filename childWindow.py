from selenium import webdriver

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\selenium\\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element_by_link_text('Click Here').click()
childWindow = driver.window_handles[1]
parentWindow = driver.window_handles[0]

driver.switch_to.window(childWindow)
print('child text is  "' + driver.find_element_by_tag_name('h3').text + '"')
driver.close()

driver.switch_to.window(parentWindow)
assert 'Opening a new window' == driver.find_element_by_tag_name('h3').text
