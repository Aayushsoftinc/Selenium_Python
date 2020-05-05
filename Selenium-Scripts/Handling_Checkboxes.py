from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# Get the list of checkboxes and put them in a variable
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# To print the count of checkboxes on a webpage
print(len(checkboxes))

#Requirement is to click on all the checkboxes

for checkbox in checkboxes:
    checkbox.click()
# to put assertion if checkbox is selected
    assert checkbox.is_selected()






