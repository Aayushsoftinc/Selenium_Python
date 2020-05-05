from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")
# Maximize the window
driver.maximize_window()
# Invoke the URL
driver.get("https://www.rahulshettyacademy.com/")

# To see the title of the webpage
print(driver.title)

# To verify we landed in correct URL
print(driver.current_url)

# Go to other webpage
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()

# To return back to the first page/URL
driver.back()
# To refresh the entire page
driver.refresh()

driver.close()