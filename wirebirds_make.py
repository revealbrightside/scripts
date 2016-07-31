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
	arr=[]
	model_arr=[]
	arr_size=0
	model_size=0

	file=open("make.csv" , "r")
	reader1 = csv.reader(file)
	for line in reader1:
		t=line[0]
		arr.insert(arr_size,t)
		arr_size=arr_size+1
	"""file1=open("model.csv","r")
	reader1=csv.reader(file1)
	for line in reader1:
		t=line[0]
		model_arr.insert(model_size,t)
		model_size=model_size+1"""


	c=csv.writer(open("WireBirds_make.csv", "wb"))
	c.writerow(["Year","Item Title","Make","Model"])
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
	driver.get('https://www.wirebids.com/auctions?closed=1')
	time.sleep(2)
	html=driver.page_source
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


			"""index1=subhtml.index('<div class="alert alert-neutral">')
			subhtml=subhtml[index1:]
			index2=subhtml.index('>')
			subhtml=subhtml[index2+1:]
			index2=subhtml.index('<')
			date=subhtml[:index2]
			date=date[15:]
			temp=date[:3]
			if temp=='Jan':
				temp='01'
			elif temp=='Feb':
				temp='02'
			elif temp=='Mar':
				temp='03'
			elif temp=='Apr':
				temp='04'
			elif temp=='May':
				temp='05'
			elif temp=='Jun':
				temp='06'
			elif temp=='Jul':
				temp='07'
			elif temp=='Aug':
				temp='08'
			elif temp =='Sep':
				temp='09'
			elif temp =='Oct':
				temp='10'
			elif temp =='Nov':
				temp='11'
			elif temp == 'Dec':
				temp='12'
			temp=temp+"/"
			index1=date.index(' ')
			date=date[index1+1:]
			index2=date.index(',')
			val=date[:index2]
			date=date[index2+2:]
			if val<10:
				val="0"+val
			#print val
			temp=temp+val+"/"
			index1=date.index(' ')
			date=date[:index1]
			year=date[-2:]
			#print year
			temp=temp+year
			date=temp


			index1=subhtml.index('<span>Seller:')
			subhtml=subhtml[index1+13:]
			index2=subhtml.index('>')
			subhtml=subhtml[index2+1:]
			index2=subhtml.index('<')
			seller=subhtml[:index2]
			

			

			index1=subhtml.index('Buyers Premium:')
			subhtml=subhtml[index1+10:]
			index1=subhtml.index('>')
			subhtml=subhtml[index1+1:]
			index1=subhtml.index('<')
			premium=subhtml[:index1]
			#print 'Buyers Premium: is ' + premium

			subpremium=premium[:-1]
			subpremium=float(subpremium)"""

			
			


			
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


						"""finalprice= (subpremium*subprice)/100
						finalprice=finalprice+subprice
						finalprice=str(finalprice)
						finalprice="$"+finalprice




						index1=subhtml.index('<a class="lot-img-link pull-right"')
						subhtml=subhtml[index1:]
						index1=subhtml.index('href="')
						subhtml=subhtml[index1+6:]
						index2=subhtml.index('"')
						link1=subhtml[:index2]
						link1=main+link1
						#print 'url is' + link1"""

						index1=subhtml.index('<span class="lot-id">')
						subhtml=subhtml[index1:]
						index2=subhtml.index('</span> ')
						subhtml=subhtml[index2+7:]
						index2=subhtml.index('</a>')
						title=subhtml[:index2]
						title=title.strip()
						year=title[:4]
						if year.isdigit():
							title=title[4:]
							title=title.strip()
						else:
							year='-'

						backup=[]
						backupsize=0

						for i in range(0,arr_size):
							arr[i]=arr[i].strip()
							if arr[i]  in title:
								index1=title.index(arr[i])
								if index1 is 0 or title[index1-1]==' ':
									temp10=title[index1+len(arr[i]):]
									if len(temp10) is 0:
										backup.insert(backupsize,arr[i])
										backupsize=backupsize+1
										make=arr[i]
										#break
									elif temp10[0]==' ':
										backup.insert(backupsize,arr[i])
										backupsize=backupsize+1
										make=arr[i]
										#break

						for k in range (0,backupsize):
							if backupsize is 1:
								make=backup[0]
							else:
								index1=title.index(backup[k])
								index2=title.index(make)
								if index1<index2:
									make=backup[k]




									
						"""for i in range (0,model_size):
							if model_arr[i] in title:
								index1=title.index(model_arr[i])
								if index1 is 0 or title[index1-1]==' ':
									temp10=title[index1+len(model_arr[i]):]
									if len(temp10) is 0:
										model=model_arr[i]
										break
									elif temp10[0]==' ':
										model=model_arr[i]
										break"""


						if ' - Click' in title:
							index1=title.index(' - Click')
							title=title[:index1]
							title=title.strip()

						"""if ' - Click' in title:
							index1=title.index(' - Click')
							temp3=title[index1+7:]
							if '-' not in temp3:
								title=title[:index1]


							
						if '- ' in title:
							index1=title.rfind('- ')
							temp=title[index1+2:]
							subtitle=title[:index1]
							index2=temp.rfind(' ')
							temp1=temp[:index2]
							temp2=temp[index2+1:]
							for i in range(0,arr_size):
								if temp2== arr[i]:
									print 'YES'
									print temp1
									print temp2
									city=temp1
									city=city.replace(',','')
									state=temp2
									title=subtitle
						if ' - Click' in title:
							index1=title.index(' - Click')
							title=title[:index1]
							title=title.strip()"""












						
						"""if arr[i] in title:
							index1=title.index(arr[i])
							temp=title[index1:]
							if ' ' in temp:
								index1=temp.index(' ')
								temp=temp[:index1]

							if temp == arr[i]:
								print temp
								print 'YES'"""
								
						"""if i!= arr_size:
							index1=title.index(temp)
							title=title[:index1]
							index2=title.rfind('-')
							city=title[index2+1:]
							title=title[:index2]
							print city
							print state"""



						"""if ',' in title:
							index1=title.rfind(',')
							temp1=title[:index1]
							temp1=temp1[-30:]
							temp2=title[index1+1:]
							temp2=temp2.strip()
							if '-' in temp1:
								index1=temp1.rfind('-')
								temp1=temp1[index1+1:]
								temp1=temp1.strip()
								if '-' in temp2:
									index2=temp2.index('-')
									temp2=temp2[:index2]
								if len(temp2)<10:
									city=temp1
									state=temp2
									print temp1
									print temp2"""








						"""index1=subhtml.index('<div class="lot-description">')
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

							serialno=serialno.replace('&nbsp;','')


							if 'S/N' in serialno:
								index1=serialno.index('S/N')
								serialno=serialno[index1+4:]
								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								#print serialno
								serial=serialno

							elif 'Serial No.' in serialno:
								index1=serialno.index('Serial No.')
								serialno=serialno[index1+11:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]


								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								#print serialno
								serial=serialno

							elif 'SN' in serialno:
								index1=serialno.index('SN')
								serialno=serialno[index1+3:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								#print serialno
								serial=serialno

							elif 'Serial Number:' in serialno:
								index1=serialno.index('Serial Number:')
								serialno=serialno[index1+15:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno


							elif 'S/n' in serialno:
								index1=serialno.index('S/n')
								serialno=serialno[index1+4:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno


							elif 'Serial' in serialno:
								index1=serialno.index('Serial')
								serialno=serialno[index1+7:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]
								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno


							elif 's/sn' in serialno:
								index1=serialno.index('s/sn')
								serialno=serialno[index1+5:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno



							elif 'Ser. #' in serialno:
								index1=serialno.index('Ser. #')
								serialno=serialno[index1+7:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno

							elif 'Serial #' in serialno:
								index1=serialno.index('Serial #')
								serialno=serialno[index1+9:]

								index2=serialno.index('<')
								temp=serialno[:index2]
								if len(temp)<2:
									index1=serialno.index('>')
									serialno=serialno[index1+1:]

								if serialno[0] == '<':
									index1=serialno.index('>')
									serialno=serialno[index1+1:]
									if serialno[0] is '<':
										index1=serialno.index('>')
										serialno=serialno[index1+1:]

								index2=serialno.index('<')
								serialno=serialno[:index2]
								serialno=serialno.strip()
								print serialno
								serial=serialno"""

						c.writerow([year,title,make,model])












					"""if '<img class="img"' in sub:
						img = driver.find_element_by_xpath('//*[@id="description"]/div/a/img')
						src = img.get_attribute('src')
						
						inc=str(counter)
						img_name=global_img+inc
						img_name=img_name+".png"
						urllib.urlretrieve(src, img_name)"""
					
					

					
					



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

