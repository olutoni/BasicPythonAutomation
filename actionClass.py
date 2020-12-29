from selenium import webdriver
from selenium.webdriver import ActionChains

# browser exposes an executable file
# through selenium test involve the executable which will invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.maximize_window()
#driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')

action = ActionChains(driver)
# menu = driver.find_element_by_id('mousehover')
#
# action.move_to_element(menu).perform()
# childMenu = driver.find_element_by_link_text('Top')
# action.move_to_element(childMenu).click().perform()
#
# action.move_to_element(menu).perform()
# childMenu2 = driver.find_element_by_link_text('Reload')
# action.move_to_element(childMenu2).click().perform()



button = driver.find_element_by_id('double-click')
action.context_click(button).perform()
action.double_click(button).perform()

alert = driver.switch_to.alert
assert 'You double clicked me!!!, You got to be kidding me' == alert.text
alert.accept()
