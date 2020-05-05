from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser
validateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
# switch to alert and assign it to a variable
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept() # To click on the okay button of an alert
driver.close()