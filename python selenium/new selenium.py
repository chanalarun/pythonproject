import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="c:/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_xpath('//a[text()="Shop"]').click()
products=driver.find_elements_by_css_selector('button[class="btn btn-info"]')
for product in products:
    product.click()
driver.find_element_by_css_selector('a[class="nav-link btn btn-primary"]').click()
driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_css_selector('#country').send_keys("ind")
time.sleep(5)
driver.find_element_by_xpath('//a[text()="India"]').click()
driver.find_element_by_css_selector('div[class="checkbox checkbox-primary"]').click()
driver.find_element_by_css_selector('input[class="btn btn-success btn-lg"]').click()
print(driver.find_element_by_css_selector('div[class="alert alert-success alert-dismissible"]').text)
driver.close()
driver.quit()