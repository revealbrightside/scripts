# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import urllib2
import urllib
import csv
import time
import re
import locale
import os
import sys
import unicodedata
import base64
#!/usr/local/bin/python
 #coding: latin-1
reload(sys)
sys.setdefaultencoding("utf_8")




def mainFunction():
	


	c=csv.writer(open("WireBirds_Description3.csv", "wb"))
	c.writerow(["Item Title","Description","Full Description"])
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
	driver = webdriver.Chrome(chrome_options=options)
	driver.maximize_window()

	driver.get('https://www.wirebids.com/')
	driver.find_element_by_xpath('//*[@id="top"]/div[1]/div/div/div/ul[2]/li[1]/a').click()
	username=driver.find_element_by_xpath('//*[@id="UserEmail"]')  
	username.clear()
	username.send_keys('office@brightsidemarkets.com')
	password=driver.find_element_by_xpath('//*[@id="UserPassword"]')  
	password.clear()
	password.send_keys('printczar2005'+'\n')
	time.sleep(1)
	driver.get('https://www.wirebids.com/auctions/index/page:10?closed=1')
	time.sleep(2)
	html=driver.page_source
	index1=html.index('Auction closed Jul 18, 2012')
	html=html[index1:]


	main="https://www.wirebids.com"
	end=1


	while end is not 0:
		global_img="image"
		counter=1

		while '<a class="thumbnail" ' in html:
			date='-'
			seller='-'
			phone='-'

			index1=html.index('<a class="thumbnail" ')
			html=html[index1:]
			index2=html.index('href="')
			html=html[index2+6:]
			index2=html.index('"')
			link=html[:index2]
			url=main+link
			driver.get(url)
			subhtml=driver.page_source


			
			flag=1
			while flag is not 0:

				while '<strong class="price">' in subhtml:
					price='-'
					title='-'
					description='-'
					img_name='-'
					serial='-'
					city='-'
					state='-'
					make='-'
					model='-'




					index1=subhtml.index('<strong class="price">')
					subhtml=subhtml[index1+22:]
					index2=subhtml.index('<')
					price=subhtml[:index2]
					#print 'price is' + price

					subprice=price.replace('$','')
					subprice=subprice.replace(',','')
					subprice=float(subprice)

					if subprice >199:
	
						index1=subhtml.index('<a class="lot-img-link pull-right"')
						subhtml=subhtml[index1:]
						index1=subhtml.index('href="')
						subhtml=subhtml[index1+6:]
						index2=subhtml.index('"')
						link1=subhtml[:index2]
						link1=main+link1

						index1=subhtml.index('<span class="lot-id">')
						subhtml=subhtml[index1:]
						index2=subhtml.index('</span> ')
						subhtml=subhtml[index2+7:]
						index2=subhtml.index('</a>')
						title=subhtml[:index2]
						title=title.strip()

						if 'letterpress woodtype' and 'letterpress wood type' not in title:
						

							index1=subhtml.index('<div class="lot-description">')
							subhtml=subhtml[index1+29:]
							index2=subhtml.index('</div>')
							description=subhtml[:index2]

							
							counter=counter+1
							driver.get(link1)
							sub=driver.page_source
							serialno=sub


							if '<div id="description"' in serialno:
								index1=serialno.index('<div id="description"')
								serialno=serialno[index1:]
								index2=serialno.index('</div>')
								serialno=serialno[index2+6:]
								index2=serialno.index('/div>')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								serialno=serialno.replace('&nbsp;','')
							else:
								serialno='-'


							

							c.writerow([title,description,serialno])






				if '<li class="next">' in subhtml:
					index1=subhtml.index('<li class="next">')
					subhtml=subhtml[index1:]
					index1=subhtml.index('<a href="')
					subhtml=subhtml[index1+9:]
					index2=subhtml.index('"')
					next1=subhtml[:index2]
					url=main+next1
					driver.get(url)
					subhtml=driver.page_source
				else:
					flag=0


	
		if '<li class="next">' in html:
					index1=html.index('<li class="next">')
					html=html[index1:]
					index1=html.index('<a href="')
					html=html[index1+9:]
					index2=html.index('"')
					next1=html[:index2]
					url=main+next1
					driver.get(url)
					html=driver.page_source
		else:
			end=0


	testVar = raw_input("Ask user for something.")



mainFunction()

