from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://login.salesforce.com/?locale=eu")
driver.maximize_window()

driver.find_element_by_css_selector("#username").send_keys("ptamhane")

driver.find_element_by_css_selector(".password").send_keys("Rambo")

# To clear all the inputs present in the edit box
driver.find_element_by_css_selector(".password").clear()

# Identify and click on the link --> check for the anchor tag -> use linktext locator

driver.find_element_by_link_text("Forgot Your Password?").click()

# Using xpath locator based on the text

driver.find_element_by_xpath("//a[text()='Cancel']").click()

# Using absolute XPATH - traversing through parent node to child
#//div[@id='usernamegroup']/label
#//form[@name='login']/div[1]/label

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

# Parent-Child traverse using CSS locator
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(2)").text)
#print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
driver.close()


