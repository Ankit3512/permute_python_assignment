from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xpath import Xpath
import time

options = Options()
options.add_argument("--incognito")
options.add_experimental_option("detach", True)
# options.add_argument('headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver,10)
driver.get("https://www.policybazaar.com/")
driver.maximize_window()

driver.implicitly_wait(10)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.car_insurance_button))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.click_here))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.select_city))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.rto_code))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.brand_type))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.model_type))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.fuel_type))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.varient_type))).click()
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, Xpath.full_name))).send_keys("Test User")
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, Xpath.mobile_no))).send_keys("9214141473")
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.view_price_button))).click()
time.sleep(15)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.confirm_otp))).click()
    time.sleep(1)
except Exception:
    pass

time.sleep(10)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.delivery_details))).click()
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, Xpath.ex_showroom_price))).send_keys("700000")
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.submit))).click()
time.sleep(10)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.refresh_button))).click()
    time.sleep(1)
except Exception:
    pass

# driver.refresh()
# wait.until(EC.presence_of_element_located((By.XPATH, Xpath.ex_showroom_price))).send_keys("7000000")
# time.sleep(1)
# wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.submit))).click()
# time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.idv_value_change))).click()
time.sleep(5)
field = wait.until(EC.presence_of_element_located((By.XPATH, Xpath.idv_value_amount_field)))

# Check current value before and after setting
print("Before clear:", field.get_attribute("value"))
field.clear()
print("After clear:", field.get_attribute("value"))
field.send_keys("500000")
print("After send_keys:", field.get_attribute("value"))

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.idv_value_update))).click()
time.sleep(5)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.addon_zero_dep))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.addon_engine_protector))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.invoice_price_cover))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath. tyre_Protector))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.accidental_cover))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.addon_paid_driver))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.accessories_cover))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.addon_electrical))).click()
time.sleep(3)

wait.until(EC.presence_of_element_located((By.XPATH, Xpath.addon_electrical_cover_amount))).send_keys("15000")
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.apply_button))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, Xpath.select_insurer))).click()
time.sleep(3)

plan_type_value = wait.until(EC.presence_of_element_located((By.XPATH, Xpath.plan_type))).text
time.sleep(1)
print("Plan Type:", plan_type_value)

idv_value = wait.until(EC.presence_of_element_located((By.XPATH, Xpath.idv))).text
time.sleep(1)
print("IDV Cover:", idv_value)

payment_value = wait.until(EC.presence_of_element_located((By.XPATH, Xpath. You_will_pay))).text
time.sleep(1)
print("You Will Pay:", payment_value)

driver.quit()