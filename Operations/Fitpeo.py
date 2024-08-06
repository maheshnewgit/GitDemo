import time
from _ast import arguments

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.fitpeo.com/")
driver.implicitly_wait(5)
driver.maximize_window()
Revenue_Calculator=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/revenue-calculator']")))
Revenue_Calculator.click()

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium css-duk49p']")))
Slider_Viewed = driver.find_element(By.XPATH,"//span[@class='MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium css-duk49p']")
driver.execute_script("arguments[0].scrollIntoView();",Slider_Viewed)
Slider_Circle = driver.find_element(By.XPATH,"//input[@type='range']")
action = ActionChains(driver)
# value=820   #93.67
# min=-30
# max=300
# slider_width = Slider_Circle.size['width']
# x_offset = ((value - min) / (max - min)) * slider_width
# print(slider_width)
action.click_and_hold(Slider_Circle).move_by_offset(271, 0).release().perform()

# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@aria-valuenow='820']")
#
# Slider_Box = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']")
# #Slider_Box.send_keys("820")
# time.sleep(5)
# Slider_Box.send_keys("20")
# time.sleep(5)
# # Slider_Box.send_keys("820")
# print(Slider_Box.text)
# time.sleep(5)

# assert Slider_Box.get_attribute('value')=='820'

# Slider_Box = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']")
# Slider_Box.send_keys("560")
# # dr = driver.execute_script("arguments[0].value = arguments[1];", Slider_Box, 560)
# # assert dr == '560'
#
# Slider_Box.clear()
# Slider_Box.send_keys('560')
# Slider_Box.send_keys(Keys.RETURN)
#
# # Validate Slider Value using JavaScript
# slider_value = driver.execute_script("return arguments[0].value;", Slider_Circle)
# assert slider_value == '560'

# cpt_codes = ['CPT-99091', 'CPT-99453', 'CPT-99454', 'CPT-99474']
# list_of_cpt_codes=driver.find_elements(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 inter css-1s3unkt']")
# for code in list_of_cpt_codes:
#     if code.text in cpt_codes:
#         checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
#         if not checkbox.is_selected():
#             checkbox.click()
#
#
# # Validate Total Recurring Reimbursement
# total_reimbursement = driver.find_element(By.XPATH, "//div[@class='MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular css-1lnu3ao']/p[4]/p")
# assert total_reimbursement.text == '$110700'

