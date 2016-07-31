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

	c=csv.writer(open("WireBirds_v4.csv", "wb"))
	c.writerow(["Year","Make","Model","SSN","Item Title","Final Price","Date","Seller Name","Sale Price","BUYER'S COMMISSION","City","State","Original Title","URL"])

	file1=open("WireBirds_Rawdata.csv","r")
	reader1=csv.reader(file1)
	for line in reader1:
		t=line[0]
		title=t
		price='-'
					
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
		url='-'


		
		temp_title=title.lower()


															

		if  'woodtype' not in temp_title and 'wood type' not in temp_title and 'type cabinet' not in temp_title and 'custom-built' not in temp_title and 'custom-made' not in temp_title and 'strathmore' not in temp_title and not temp_title.startswith('pallet of') and not temp_title.startswith('brand new'):

			if ' ' in title:
				index1=title.index(' ')
				temp=title[:index1]
				if temp.isdigit() and len(temp)==4:
					title=title[4:]
					title=title.strip()
					year=temp

				if 'YEAR' in title:
					index1=title.index('YEAR')
					tt=title[index1+4:]
					index2=tt.index(' ')
					tt=tt[index2+1:]
					tt=tt.strip()
					t1=tt[:4]
					if t1.isdigit():
						year=t1
						if 'CIRCA' in title:
							title=title[:index1]
							title=title + 'CIRCA'
						else:
							title=title[:index1]



						
					else:
						if ' ' in tt:
							index2=tt.index(' ')
							tt=tt[index2+1:]
							tt=tt.strip()
							t1=tt[:4]
							if t1.isdigit():
								year=t1

								if 'CIRCA' in title:
									title=title[:index1]
									title=title + 'CIRCA'
								else:
									title=title[:index1]


							else:
								if ' ' in tt:
									index2=tt.index(' ')
									tt=tt[index2+1:]
									tt=tt.strip()
									t1=tt[:4]
									if t1.isdigit():
										year=t1
										if 'CIRCA' in title:
											title=title[:index1]
											title=title + 'CIRCA'
										else:
											title=title[:index1]


									else:
										if ',' in title:
											index1=title.index('YEAR')
											tt=title[index1+4:]
											index2=tt.index(',')
											tt=tt[:index2]
											tt=tt[-4:]
											
											if tt.isdigit():
												year=tt
												if 'CIRCA' in title:
													title=title[:index1]
													title=title + 'CIRCA'
												else:
													title=title[:index1]


				






					
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

						elif temp10[0].isalpha() or temp10[0].isdigit():
							continue;
						else:
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

			if make !='hamilton' and make !='international paper':


				if make is not '-':
					index1=title.index(make)
					tt=title[index1:]
					tt=tt.strip()
					

					for k in range (0,sc_size):
						i=specialcase[k] + ' '

						if i in tt:
							index1=tt.index(i)
							tt=tt[index1:]
							tt=tt[:len(i)]
							if make in tt:
								index1=tt.index(make)
								tt=tt[index1+len(make):]
								model=tt
								model=model.strip()
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
				finalprice=line[1]
				date=line[2]
				seller=line[3]
				price=line[4]
				commision=line[5]
				subprice=price[1:]
				subprice=subprice.replace(',','')
				subprice=float(subprice)
				serial=line[6]
				url=line[7]
				if make=='-' and  model =='-':
					if subprice>999 and 'assorted' not in title:					 
						c.writerow([year,make,model,serial,lowerTitle,finalprice,date,seller,price,commision,city,state,originalTitle,url])
				else:
					c.writerow([year,make,model,serial,lowerTitle,finalprice,date,seller,price,commision,city,state,originalTitle,url])


					






				


	testVar = raw_input("Ask user for something.")

	
	



mainFunction()

