from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from confi import *


infofill=[ ]


# def excel_tableprint(infofill):
#     # spl = str(datetime.datetime.now()).split(':')
#     shtname = str(datetime.date.today())#spl[0] #+ '-' + spl[1]
#
#
#     # lode excel file
#     wb = openpyxl.load_workbook('hello.xlsx')
#
#
#     t=wb.get_active_sheet
#
#
#     # creat a sheet loop
#
#     # if t == shtname:
#     #     print(t)
#     #     print("its a ,atch")
#     # else:
#     #     wb.create_sheet(shtname)
#     #     wb.active=-1
#     #     print("here")
#
#     print(wb.sheetnames)
#     print(wb.active)
#     ws = wb.active
#
#     ws.append([" Entry No. ", " Flat No. ", " CustomerID ", " Date ", " Amount "])
#     for column in infofill:
#         ws.append(column)
#
#     tab = Table(displayName="Table1", ref="A1:E5")
#     style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
#                            showLastColumn=False, showRowStripes=True, showColumnStripes=True)
#     tab.tableStyleInfo = style
#     ws.add_table(tab)
#
#     wb.save('hello.xlsx')



def Dgvcl(coustomer_number):
    # create a new chrome session
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome('./chromedriver',options=chrome_options)

    # firefox
    # driver = webdriver.Firefox(executable_path="/Users/divyesh/Documents/PycharmProjects/BOT/Geb bot/geckodriver")
    firefox_profile = webdriver.FirefoxProfile()  # browser driver
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)  # privet window search
    options = Options()  # Fire fox optiuon
    options.headless = True  # no browser
    #
    driver = webdriver.Firefox(firefox_profile=firefox_profile,
                               executable_path="/Users/divyesh/Documents/PycharmProjects/BOT/Geb bot/geckodriver")
    # driver = webdriver.Firefox
    # (options=options,firefox_profile=firefox_profile,executable_path="/Users/divyesh/Documents/PycharmProjects/BOT/
    # Geb bot/geckodriver")

    # Navigate to the application home page
    driver.get(signup_url)

    x = coustomer_number  # consumer number feeding variable
    loop = 0  # loop value

    driver.minimize_window()

    # loop start
    while True:
        if loop <= len(x)-1:  # loop set at the the numerical value of loop loop
            # :runstillitissmaller then number of id to be fed
            time.sleep(2)

            # Customer id is in a format of "(fla no).(customerIDnO)" :. code below splits and provides just the iD No
            p = x[loop].split('.')[-1]
            q = x[loop].split('.')[0]

            # get the search textbox and type the customer id number
            driver.find_element_by_xpath('//*[@id="idConsumerNo"]').send_keys(p)

            # # # wait till submit button loads
            # butrpap = driver.find_element_by_xpath()
            #
            # driver.execute_script("arguments[0].style.visibility='hidden'", butrpap)

            # blur = WebDriverWait(driver, delay).until(EC.presence_of_element_located
            # ((By.XPATH, '//*[@id="idWaitBack"]')))
            # print("Page is ready!")

            ###################################

            delay = 100
            try:
                WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSubmit"]/span')))
            except TimeoutException:
                print('it took longer then i %s Sec' % delay)

            # submit
            driver.find_element_by_xpath('//*[@id="idSubmit"]/span').click()

            # wait till bill date loads
            delay = 100
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located
                                                            ((By.ID, 'idBillMonthYearLabel')))
                # print("Page is ready!")
            except TimeoutException:
                print("Loading took too much more time then %s Sec" % delay)

            # wait till the submit button is clickable as the values will be refrashed
            delay = 100
            try:
                WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSubmit"]/span')))
            except TimeoutException:
                print('it took longer then %s Sec' % delay)
                # get Date Amount And id

            user_date = driver.find_element_by_xpath('//*[@id="idBillMonthYear"]').get_attribute('value')  # date
            user_amount = driver.find_element_by_xpath('//*[@id="idAmount"]').get_attribute('value')  # amount


            # return valus and info

            infotoken = ['%s'%loop,'%s'%q,'%s'%p,'%s'%user_date,'%s'%user_amount]
            infofill.extend([infotoken])
            # print(infofill)
            print(len(infofill))
            print(infotoken)
            # print("EntryNo: %s"%loop)
            # print("FlatNo: %s"%q)
            # print("CustomerID: %s"%p+" Date: %s"%user_date+" Amount: %s"%user_amount)


            # clear after submit
            driver.find_element_by_xpath('//*[@id="idConsumerNo"]').send_keys(Keys.COMMAND+'a')


            # loop rounds count
            loop += 1
            print()
        else:
            # close the browser
            driver.quit()
            break





if __name__ == '__main__':
    Dgvcl(coustomer_number)

