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
	states=[]
	model_arr=[]
	arr_size=0
	state_size=0
	model_size=0
	specialcase=[]
	sc_size=0


	file=open("states.csv" , "r")
	reader1 = csv.reader(file)
	for line in reader1:
		t=line[0]
		states.insert(state_size,t)
		state_size=state_size+1


	file=open("correct_make.csv" , "r")
	reader1 = csv.reader(file)
	for line in reader1:
		t=line[0]
		t=t.lower()
		arr.insert(arr_size,t)
		arr_size=arr_size+1

	
	file1=open("correct_model.csv","r")
	reader1=csv.reader(file1)
	for line in reader1:
		t=line[0]
		t=t.lower()
		model_arr.insert(model_size,t)
		model_size=model_size+1

	file1=open("sc.csv","r")
	reader1=csv.reader(file1)
	for line in reader1:
		t=line[0]
		t=t.lower()
		specialcase.insert(sc_size,t)
		sc_size=sc_size+1


	c=csv.writer(open("WireBirds_v2.csv", "wb"))
	c.writerow(["Year","Make","Model","Item Title","Final Sale Price","SALE DATE","SELLER NAME","Sale Price","BUYER'S COMMISSION","City","State","Original Title"])
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


			index1=subhtml.index('<div class="alert alert-neutral">')
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
			subpremium=float(subpremium)

			
			


			
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



					index1=subhtml.index('<strong class="price">')
					subhtml=subhtml[index1+22:]
					index2=subhtml.index('<')
					price=subhtml[:index2]
					#print 'price is' + price

					subprice=price.replace('$','')
					subprice=subprice.replace(',','')
					subprice=float(subprice)

					if subprice >199:


						finalprice= (subpremium*subprice)/100
						finalprice=finalprice+subprice
						finalprice=str(finalprice)
						finalprice="$"+finalprice




						"""index1=subhtml.index('<a class="lot-img-link pull-right"')
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
						title=title.replace('â','')
						title=title.replace('amp;','')
						title=title.replace('€','"')
						title=title.replace('ï»¿','')
						

						if 'letterpress woodtype' and 'letterpress wood type' not in title:
							if ' ' in title:
								index1=title.index(' ')
								temp=title[:index1]
								if temp.isdigit() and len(temp)==4:
									title=title[4:]
									title=title.strip()
									year=temp
								elif 'YEAR ' in title:
									index1=title.index('YEAR ')
									tt=title[index1+5:]
									tt=tt.strip()
									tt=tt[:4]
									if tt.isdigit():
										year=tt
								elif 'YEAR: ' in title:
									index1=title.index('YEAR: ')
									tt=title[index1+6:]
									tt=tt.strip()
									tt=tt[:4]
									if tt.isdigit():
										year=tt
								elif 'YR ' in title:
									index1=title.index('YR ')
									tt=title[index1+3:]
									tt=tt.strip()
									tt=tt[:4]
									if tt.isdigit():
										year=tt


							



							words1 = set(title.split())


							for i in range (0,state_size):
								if states[i] in words1:
									state=states[i]
									print 'State is' + state

									index1=title.rfind(state)
									title=title[:index1-1]
									title=title.strip()
									temp3=title[-20:]
									temp3.strip()
									if '- ' in temp3:
										index2=title.rfind('- ')
										title=title[:index2]
										title=title.strip()
										index1=temp3.rfind('- ')
										temp3=temp3[index1+2:]
									else:
										#index2=title.rfind('- ')
										#title=title[:index2]
										#title=title.strip()
										#index1=temp3.rfind(' ')
										#temp3=temp3[index1+1:]
										temp3='-'
									city=temp3
									city=city.replace(',','')
									print 'City is' + city
							originalTitle=title
							title=title.lower()		

							if ' - click' in title:
								index1=title.index(' - click')
								title=title[:index1]
								title=title.strip()

							lowerTitle=title


							backup=[]
							backupsize=0


							for i in range(0,arr_size):
								if arr[i]  in title:
									index1=title.index(arr[i])
									if index1 is 0 or title[index1-1]==' ' or title[index1-1]=='-' or title[index1-1]=='/':
										temp10=title[index1+len(arr[i]):]
										if len(temp10) is 0:
											backup.insert(backupsize,arr[i])
											backupsize=backupsize+1
											make=arr[i]
											#print make
											#break
										elif temp10[0]==' ' or temp10[0]=='-' or temp10[0]=='/' or temp10[0]==',':
											backup.insert(backupsize,arr[i])
											backupsize=backupsize+1
											make=arr[i]
											#print make
											#break
							temp12=title

							for k in range (0,backupsize):
								if backupsize is 1:
									make=backup[0]
									index1=title.index(make)
									temp12=title[index2+4:]
								else:
									index2=title.index(make)
									index1=title.index(backup[k])
									
									if index1<index2:
										make=backup[k]
										temp12=title[index1+4:]
									else:
										temp12=title[index2+4:]
							print 'Make is' + make


							if make is not '-':
								index1=title.index(make)
								tt=title[index1+len(make):]
								tt=tt.strip()
								words1 = set(tt.split())


								for k in range (0,sc_size):

									if specialcase[k] in words1:
										index1=tt.index(specialcase[k])
										if index1 is 0:
											tti=tt[index1+len(specialcase[k]):]

											if len(tti) is not 0:
												if tti[0] == ' ':
													model=specialcase[k]
													print 'Special Case Model is' + model
													break
											else:
												model=specialcase[k]
												print 'Special Case Model is' + model
												break



											


							if model is '-':
								backup_model=[]
								backupsize_model=0		

								for i in range (0,model_size):
									if model_arr[i] in title:
										index1=title.index(model_arr[i])
										if index1 is 0 or title[index1-1]==' ':
											temp10=title[index1+len(model_arr[i]):]
											if len(temp10) is 0:
												backup_model.insert(backupsize_model,model_arr[i])
												backupsize_model=backupsize_model+1
												model=model_arr[i]

											elif temp10[0]==' ' or temp10[0]==',' or temp10[0]=='-' or temp10[0]=='/' or temp10[0]==')':
												backup_model.insert(backupsize_model,model_arr[i])
												backupsize_model=backupsize_model+1
												model=model_arr[i]

								temp12=title

								for k in range (0,backupsize_model):
									if backupsize_model is 1:
										model=backup_model[0]
										index1=title.index(model)
										temp12=title[index2+4:]
									else:
										index2=title.index(model)
										index1=title.index(backup_model[k])
										
										if index1<index2:
											model=backup_model[k]
											temp12=title[index1+4:]
										else:
											temp12=title[index2+4:]


								print 'Model is' + model
							

							c.writerow([year,make,model,lowerTitle,finalprice,date,seller,price,premium,city,state,originalTitle])

					



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

