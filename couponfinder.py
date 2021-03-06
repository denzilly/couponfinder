from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from random import *

import csv

import time

############LIST OF XPATHS##############

expired = '//*[@id="validation_close_button"]'

delbtn = '//*[@id="delivery"]'
pstcd = '//*[@id="customer-postcode"]'
huis = '//*[@id="customer-street-no"]'
next = '//*[@id="order-time-button"]'
adbtn = '/html/body/div[3]/div[2]/div/section/ul[1]/li/a'
coup = '//*[@id="voucher_code"]'
coupbtn = '//*[@id="apply_voucher"]'

coupmsg = '/html/body/div[12]/div[2]/div/div[1]/ul/li'
coupclose = '//*[@id="validation_close_button"]'
coupdesc = '/html/body/div[6]/section/section/div[2]/section[2]/div/div[4]/div/div[1]/div/div[1]/div[1]'
coupdel = '/html/body/div[6]/section/section/div[2]/section[2]/div/div[4]/div/div[1]/div/div[2]/a'




def main(rangemin,rangemax):


    codes = []

    wts = 0.9
    wtl = 3


    driver = webdriver.Firefox()
    driver.get("https://bestellen.dominos.nl/estore/nl/ProductMenu")


    time.sleep(wts)
    driver.find_element_by_xpath(expired).click()
    time.sleep(wts)
    driver.find_element_by_xpath(delbtn).click()
    time.sleep(wts)

    driver.find_element_by_xpath(pstcd).send_keys("6222ah")
    driver.find_element_by_xpath(huis).send_keys("77")
    driver.find_element_by_xpath(next).click()
    time.sleep(wts)


    driver.find_element_by_xpath(adbtn).click()

    time.sleep(wts)

    #in case shop is closed
    try:
        driver.find_element_by_xpath('//*[@id="order_time_select"]').click()
        driver.find_element_by_xpath('//*[@id="order_time_select"]').send_keys('1')
        driver.find_element_by_xpath('//*[@id="start-order-button"]').click()
    except:
        print("store is open")




    time.sleep(wtl)

    for x in range(rangemin, rangemax):
        try:
            driver.find_element_by_xpath(coup).send_keys(x)
            driver.find_element_by_xpath(coupbtn).click()
            time.sleep(wts)
        except:
            print("error")
            time.sleep(wtl)
            continue
        try:
            ht = driver.find_element_by_xpath(coupmsg).text
            driver.find_element_by_xpath(coupclose).click()
        except:
            try:
                codes.append((str(x) + driver.find_element_by_xpath(coupdesc).text))
                print(str(x) + driver.find_element_by_xpath(coupdesc).text)
                driver.find_element_by_xpath(coupdel).click()
                continue
            except:
                time.sleep(wtl)
                continue

        time.sleep(wts)
    print(codes)
    with open('coupons.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in codes:
            writer.writerow([row])

    csvFile.close()
    driver.close()


main(10000,20000)
