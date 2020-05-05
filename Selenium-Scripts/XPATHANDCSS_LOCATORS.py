# ********************** CSS TAG NAME ******************************************

# tagname[attribute='value'] -> tagname is optional
# Reg- [attribute*='value']
# By Id = tagname#id
# By class = tagname.className

#Tip : css is faster locator in selenium to identify the elements

# ********************** XPATH TAG NAME ******************************************
# //tagname[@attribute='value'] -> tagname is optional
#  Reg - //[contains(@attribute,'value')]
# text - //tagname[text()='xxx']

#---------------------------------------------------------------------------------

from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# Populate Name field using CSS locator and send input to edit box
driver.find_element_by_css_selector("input[name='name']").send_keys("Pushkar")

# Populate Email field using XPATH Locator and send input to edit box
driver.find_element_by_xpath("//input[@name='email']").send_keys("ptamhane@gmail.com")
# Click on the checkbox
driver.find_element_by_id("exampleCheck1").click()
# click on student checkbox
driver.find_element_by_id("inlineRadio1").click()

# click on submit
driver.find_element_by_xpath("//input[@type='submit']").click()

# Grab the text for validation using text method
print(driver.find_element_by_class_name("alert-success").text)
#Close the browser
driver.close()


