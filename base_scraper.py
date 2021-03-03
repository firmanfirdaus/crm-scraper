import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from helpers import wait_until
import constants

def main():

    profile = webdriver.FirefoxProfile("Z:/05 Profiles/SeleniumFF")
    driver = webdriver.Firefox(profile)
    driver.get(constants.APPROWEB_URL)

    # Login
    wait_until('#LoginForm_ip', 'present', driver)
    field_username = driver.find_element_by_id('LoginForm_ip')
    field_password = driver.find_element_by_id('LoginForm_kataSandi')

    field_username.send_keys(constants.APPROWEB_USER)
    field_password.send_keys(constants.APPROWEB_PASSWORD)
    field_password.send_keys(Keys.RETURN)

    wait_until('#notifPopup button', 'clickable', driver)
    driver.find_element_by_css_selector('#notifPopup button').click()

    driver.get(constants.APPROWEB_URL + 'index.php?r=crmAwas2019/petarisiko19')

    # WebDriverWait(driver, 60).until(EC.element_to_be_clickable((
    #     By.CSS_SELECTOR, '#s2id_CrmAwasModel19_wilayah > a.select2-choice')))
    wait_until('#s2id_CrmAwasModel19_wilayah > a.select2-choice', 'clickable', driver)
    driver.find_element_by_css_selector(
        '#s2id_CrmAwasModel19_wilayah > a.select2-choice').click()
    dropdown_wilayah = driver.find_element_by_css_selector(
        "#select2-drop:not([style*='display: none'])")

    dropdown_wilayah.find_element_by_xpath(
        "//div[contains(text(), 'BANDA ACEH')]").click()
    driver.find_element_by_css_selector('#yw0 input[type="submit"]').click()
    sleep(3)

    # WebDriverWait(driver, 60).until(EC.element_to_be_clickable((
    #     By.CSS_SELECTOR, '.portlet-title .actions > a')))
    wait_until('.portlet-title .actions > a', 'clickable', driver)
    driver.find_element_by_css_selector('.portlet-title .actions > a').click()
    # wait until #employee-grid_processing display:none
    # WebDriverWait(driver, 60).until(
    #     EC.invisibility_of_element_located((By.ID, 'employee-grid_processing')))
    wait_until('#employee-grid_processing', 'invisible', driver)
    driver.find_element_by_css_selector(
        '#employee-grid_filter label input').send_keys('025618133101000')

    driver.find_element_by_id('tombolCari').click()
    # WebDriverWait(driver, 60).until(
    #     EC.invisibility_of_element_located((By.ID, 'employee-grid_processing')))
    
    wait_until('#employee-grid_processing', 'invisible', driver)
    driver.find_element_by_css_selector(
        '#employee-grid tbody tr:first-child td:nth-child(3) a').click()

    # WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located((By.ID, 'profilRisiko')))
    wait_until('#profilRisiko', 'present', driver)
    petaRisiko = driver.find_element_by_id("profilRisiko")

    # for row in petaRisiko.find_elements_by_css_selector('tr'):
    #     for cell in row.find_elements_by_css_selector('td'):
    #         print(cell.text)

    # with open('peta_risiko.csv', 'w', newline='') as csvfile:
    #     wr = csv.writer(csvfile)
    #     for row in petaRisiko.find_elements_by_css_selector('tr'):
    #         for cell in row.find_elements_by_css_selector('td'):
    #             print(cell.text)
    #             wr.writerow(cell.text)

    driver.get(petaRisiko.find_elements_by_css_selector(
        'tbody a')[2].get_attribute('href'))
    outputTable = driver.find_elements_by_css_selector('#output table')[-1]

    with open('outputRisiko.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for row in outputTable.find_elements_by_css_selector('tr'):
            currentRow = []

            for cell in row.find_elements_by_css_selector('th > div'):
                currentRow.append(cell.get_attribute('innerHTML'))

            for cell in row.find_elements_by_css_selector('td'):
                currentRow.append(cell.text)

            print(currentRow)
            wr.writerow(currentRow)

# with open('eggs.csv', 'w', newline='') as csvfile:
#     wr = csv.writer(csvfile)
#     for row in table.find_elements_by_css_selector('tr'):
#         wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])

    # link_x3y3 = driver.find_element_by_css_selector('#placeholder3 .pieLabel > a').get_attribute('href')
    # driver.get(link_x3y3)

    # driver.find_element_by_id('KPPEditable').click()
    # sleep(30)
    # driver.find_element_by_css_selector('#KPPEditable .select2-arrow').click();
    # sleep(30)
    # dropdownKPP = driver.find_element_by_css_selector("#select2-drop:not([style*='display: none'])")
    # driver.find_element_by_id('kuadranEditable').click()
    # driver.get(APPROWEB_URL + 'index.php?r=home/logout')
    # sleep(5)
# employee-grid_processing
    # driver.close()


if __name__ == "__main__":
    main()
