#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.chrome.options import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import time
#ise assignment 1
driver=webdriver.Chrome(r"/usr/bin/chromedriver")
driver.get("https://github.com/login")
email = driver.find_element_by_id("login_field")
pwd = driver.find_element_by_id("password")
signin=driver.find_element_by_name("commit")
email.send_keys("richa195")
pwd.send_keys("richa@195")
signin.click()
search = driver.find_element_by_name("q")
search.send_keys("games")
search.send_keys(Keys.ENTER)
file=open("cs18m010.txt","w")
for i in range(1,5):
	Title = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[1]/a")
	update = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/div[2]") 
	stars = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/div[1]/a")
		#issues=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/a")
		#circles = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/div[2]/span/
	#span[2]") 
	description=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/p")
	#print("type", type(Title.text))
	file.writelines(str(Title.text.encode("unicode_escape")+"\n"))
	file.writelines(str(description.text.encode("unicode_escape")+"\n"))
	file.writelines(str(update.text.encode("unicode_escape"))+"\n")
	file.writelines(str(stars.text.encode("unicode_escape"))+"\n")

	file.writelines("----------------------------\n") 

for j in range(5,10):
	st = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(j)+"]/div[2]/div[2]/div/div[1]/a")
	#print(st.text)        
	tle=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(j)+"]/div[2]/div[1]/a")
	#print(tle.text)
	description=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(j)+"]/div[2]/p")
	#print(description.text)
	file.writelines(str(tle.text.encode("unicode_escape")+"\n"))
	file.writelines(str(description.text.encode("unicode_escape")+"\n"))
	file.writelines(str(st.text.encode("unicode_escape")+"\n"))
	file.writelines("----------------------------\n") 
        
file.close()        
        
        
        
 
''''for k in range(2, 10):
	#driver.get("https://github.com/search?p="+str(k)+"&q=games&type=Repositories&utf8=%E2%9C%93")
	#if k%2!=0:
	#	for i in range(1,5):
	#		stars = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/div[1]/a")
	#		print(stars.text)
	#	for j in range(5,10):
	#		st = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(j)+"]/div[2]/div[2]/div/div[1]/a")
	#		print(st.text)
	#else:
	#	for i in range(1,5):
	#		st = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(j)+"]/div[2]/div[2]/div/div[1]/a")
	#		print(st.text)
	#	for j in range(5,10):
	#		stars = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[2]/div[2]/div[1]/a")
	#		print(stars.text)
'''
