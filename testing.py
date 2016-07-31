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
	


	c=csv.writer(open("WireBirds_Rawdescription6.csv", "wb"))
	c.writerow(["Item Title","Description","Serial Number","URL"])
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
	driver = webdriver.Chrome(chrome_options=options)
	driver.maximize_window()


	driver.get('https://www.wirebids.com/')
	driver.find_element_by_xpath('//*[@id="top"]/div/div[1]/div/div/div/ul[2]/li[1]/a').click()
	username=driver.find_element_by_xpath('//*[@id="UserEmail"]')  
	username.clear()
	username.send_keys('office@brightsidemarkets.com')
	password=driver.find_element_by_xpath('//*[@id="UserPassword"]')  
	password.clear()
	password.send_keys('printczar2005'+'\n')
	time.sleep(1)
	driver.get('https://www.wirebids.com/auctions?closed=1')
	time.sleep(2)
	html=driver.page_source
	main="https://www.wirebids.com"
	end=1

	#index1=html.index('Auction closed Dec  6')
	#html=html[index1+10:]
	
	


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
					originalTitle='-'
					lowerTitle='-'
					year='-'
					link1='-'
					keyword='-'



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
						title=title.replace('â','')
						title=title.replace('amp;','')
						title=title.replace('€','"')
						title=title.replace('ï»¿','')
						if 'letterpress woodtype' and 'letterpress wood type' not in title:
							index1=subhtml.index('<div class="lot-description">')
							subhtml=subhtml[index1+29:]
							index2=subhtml.index('</div>')
							description=subhtml[:index2]
							description=description.strip()

							if 'S/N' in description:
								keyword='S/N'
								


							elif 'Serial No.' in description:
								keyword='Serial No.'

							elif 'Serial Number' in description:
								keyword='Serial Number'


							elif 'Ser. #' in description:
								keyword='Ser. #'

							elif 'Serial #' in description:
								keyword='Serial #'

							elif 'Serial' in description:
								keyword='Serial'

							elif 'S/n' in description:
								keyword='S/n'

							elif 's/sn' in description:
								keyword='s/sn'

							elif 'SN' in description:
								keyword='SN'




							if keyword is not '-':
								driver.get(link1)
								sub=driver.page_source
								serialno=sub


								if '<div id="description"' in serialno:
									index1=serialno.index('<div id="description"')
									serialno=serialno[index1:]
									index2=serialno.index('</div>')
									temp=serialno[:index2]
									if keyword in temp:
										serialno=temp
										serialno=serialno.replace('&nbsp;','')
									else:
										serialno=serialno[index2+6:]
										if '<div id="lot-thumbnails"' in serialno:
											index2=serialno.index('<div id="lot-thumbnails"')
											serialno=serialno[:index2]
											serialno=serialno.strip()
											serialno=serialno.replace('&nbsp;','')

									chepi=0
									if keyword in serialno:
										index1=serialno.index(keyword)
										serialno=serialno[index1+len(keyword):]
										index2=serialno.index('<')
										temp=serialno[:index2]
										temp=temp.replace(': ','')
										temp=temp.strip()
										if len(temp)<2:
											index1=serialno.index('>')
											serialno=serialno[index1+1:]
											serialno=serialno.strip()
											temp=serialno
											if ' ' in serialno:
												index1=serialno.index(' ')
												temp=serialno[:index1]
											if 'Number' in temp:
												index1=serialno.index('>')
												serialno=serialno[index1+1:]
												serialno=serialno.strip()



										while serialno[0] == '<':
											index1=serialno.index('>')
											serialno=serialno[index1+1:]
											if serialno[0] is '<':
												index1=serialno.index('>')
												serialno=serialno[index1+1:]

										index2=serialno.index('<')
										serialno=serialno[:index2]
										serialno=serialno.replace(': ','')


										if '(' in serialno:
											index1=serialno.index('(')
											serialno=serialno[:index1]

										if ',' in serialno:
											index1=serialno.index(',')
											serialno=serialno[:index1]

										if 'S/N' in serialno:
											index1=serialno.index('S/N')
											serialno=serialno[index1+3:]
										serialno=serialno.strip()
										serial=serialno
										serial=serial.replace('#.','')
										serial=serial.replace('#','')
										serial=serial.replace('">','')
										serial=serial.replace('Â','')
										serial=serial.strip()
										if serial.startswith('-') or serial.startswith(':'):
											serial=serial[1:]
											serial=serial.strip()
										if len(serial)>30:
											serial=serial[:30]
											if ' ' in serial:
												index1=serial.index(' ')
												if index1<3:
													temp1=serial[:index1+1]
													serial=serial[index1+1:]
													index1=serial.index(' ')
													serial=serial[:index1]
													serial=temp1+serial
													serial=serial.strip()
												else:
													serial=serial[:index1]
													serial=serial.strip()
										serial="'"+serial


										print 'Keyword is' + keyword
										#print serial







									


							c.writerow([title,description,serial,link1])

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
						