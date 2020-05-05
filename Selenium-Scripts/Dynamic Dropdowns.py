import time

from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
# Invoke the URL
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

driver.find_element_by_id("fromCity").click()

driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")

time.sleep(2)
# putting all the cities list in a variable
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))

#Use the for loop to identify a city
for city in cities:
   print(city.text)
   if city=="Del Rio, United States":
        city.click()
        break # To optimize the code after you find the city you need
