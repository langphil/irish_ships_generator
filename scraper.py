from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import re, os, config
import pandas as pd


url = config.CONFIG['url']

res = []
failedPages = []

def setupSelenium():
	options = Options()
	options.set_headless(headless=True)

	return webdriver.Firefox(firefox_options=options)

def setupDriver(driver, num):
	driver.get(url + str(num))
	WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'queryResults')))

	tbody = driver.find_element_by_xpath("//table[@id='queryResults']/tbody")
	rows = tbody.find_elements_by_xpath("tr")

	return len(rows)

def resetDriver(driver, num):
	driver.close
	driver = setupSelenium()

	return setupDriver(driver, num)

def setupBeautifulSoup(driver):
	soup = BeautifulSoup(driver.page_source, "html.parser")
	table = soup.find('table', attrs={'id':'queryResults'})

	return table.find_all('tr')

def loadWebpage(driver, num):
	rowCount = setupDriver(driver, num)

	while rowCount < 50:
		print 'ERROR: only %s rows found, reattempting load of DOM...' %(rowCount)
		failedPages.append(num)
		rowCount = resetDriver(driver, num)

def getTable(driver, res, num):
	table_rows = setupBeautifulSoup(driver)

	print "%s rows scraped and saved to csv from page %s" %(len(table_rows) - 2, num)

	for tr in table_rows:
		td = tr.find_all('td')
		row = [tr.text.strip() for tr in td if tr.text.strip()]
		if row: res.append(row)

def saveToCSV(res, num):
	df = pd.DataFrame(res)
	df = cleanDataframe(df)
	df.to_csv('data/raw.csv', header=None, mode='a', index = False)

def cleanDataframe(df):
	cols = [4, 6]
	df.drop(df.columns[cols],axis=1,inplace=True)

	df = df[[1, 0, 2, 3, 5, 7]]

	return df

def urlLoopAndScrape(res):
	for num in range(1495, 1994):
		driver = setupSelenium()

		loadWebpage(driver, num)
		getTable(driver, res, num)
		saveToCSV(res, num)

		res = []
		driver.close()

	print 'Scraping complete'
	print failedPages

urlLoopAndScrape(res)