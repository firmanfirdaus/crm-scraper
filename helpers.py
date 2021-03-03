from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(locator, condition, driver, timeout=90, by=By.CSS_SELECTOR):
    if condition == 'clickable':
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    elif condition == 'present':
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
    elif condition == 'invisible':
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((by, locator)))