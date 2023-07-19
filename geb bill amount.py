# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from confi import *

infofill = []

def Dgvcl(coustomer_number):
    # Create a new Firefox session
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path="/Users/divyesh/Documents/PycharmProjects/BOT/Geb bot/geckodriver")

    # Navigate to the application home page
    driver.get(signup_url)

    x = coustomer_number  # Customer number feeding variable
    loop = 0  # Loop value

    driver.minimize_window()

    # Loop start
    while True:
        if loop <= len(x) - 1:  # Loop runs until it reaches the number of IDs to be fed
            time.sleep(2)

            # Customer ID is in the format of "(flat no).(customerIDNo)". The code below splits and provides just the ID No
            p = x[loop].split('.')[-1]
            q = x[loop].split('.')[0]

            # Find the search textbox and type the customer ID number
            driver.find_element_by_xpath('//*[@id="idConsumerNo"]').send_keys(p)

            ###################################

            delay = 100
            try:
                WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSubmit"]/span')))
            except TimeoutException:
                print('It took longer than %s seconds' % delay)

            # Submit the form
            driver.find_element_by_xpath('//*[@id="idSubmit"]/span').click()

            # Wait till the bill date loads
            delay = 100
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located
                                                            ((By.ID, 'idBillMonthYearLabel')))
            except TimeoutException:
                print("Loading took more time than %s seconds" % delay)

            # Wait till the submit button is clickable as the values will be refreshed
            delay = 100
            try:
                WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSubmit"]/span')))
            except TimeoutException:
                print('It took longer than %s seconds' % delay)

            # Get Date, Amount, and ID
            user_date = driver.find_element_by_xpath('//*[@id="idBillMonthYear"]').get_attribute(
                'value')  # date
            user_amount = driver.find_element_by_xpath('//*[@id="idAmount"]').get_attribute(
                'value')  # amount

            # Return values and info
            infotoken = ['%s' % loop, '%s' % q, '%s' % p, '%s' % user_date, '%s' % user_amount]
            infofill.extend([infotoken])
            print(len(infofill))
            print(infotoken)
            print()

            # Clear the input field after submit
            driver.find_element_by_xpath('//*[@id="idConsumerNo"]').send_keys(
                Keys.COMMAND + 'a')  # macOS
            # driver.find_element_by_xpath('//*[@id="idConsumerNo"]').send_keys(Keys.CONTROL + 'a')  # Windows

            # Increment the loop counter
            loop += 1
        else:
            # Close the browser
            driver.quit()
            break

if __name__ == '__main__':
    Dgvcl(coustomer_number)
