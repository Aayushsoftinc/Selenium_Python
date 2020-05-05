from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://www.rahulshettyacademy.com/")

# To see the title of the webpage
print(driver.title)

# To verify we landed in correct URL
print(driver.current_url)

#To close the URL once the test is done
driver.close()