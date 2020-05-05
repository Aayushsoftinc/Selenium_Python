from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# Find element by name locator and send input to edit box
driver.find_element_by_name("name").send_keys("Pushkar")

# Enter details for Email
driver.find_element_by_name("email").send_keys("pushkar.tamhane@yahoo.ca")
# Click on the checkbox
driver.find_element_by_id("exampleCheck1").click()
# click on student checkbox
driver.find_element_by_id("inlineRadio1").click()


