
# Explicit Wait - target only specific element
# Pause the test for few seconds using time class e.x time.sleep(2)
import time

from selenium import webdriver
# browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\e-Commerce Project\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")

# Invoke the URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(4)
# Select the products based on the search
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

# Select and click on all the ADD TO CART buttons for  returned items
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# Use for loop to select all the buttons

for button in buttons:
    button.click()
# click on shopping basket icon
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Enter Explicit wait
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

#Enter Promo Code

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, ".promoInfo"))
print(driver.find_element_by_css_selector(".promoInfo").text)

#message = driver.find_element_by_css_selector("span.promoInfo").text
#print(message)
