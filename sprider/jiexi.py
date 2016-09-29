# -*-coding:utf-8 -*- 
import urllib.request  
import bs4
from bs4 import BeautifulSoup  
import re  
import io 
import sys
PATH = "tt4.txt"

f = open(PATH, "r",encoding ="utf-8", errors='ignore')
str1 = f.read()  #不能用readlines，因为它返回的是列表，而read返回的是字符串

f.close()
#soup = BeautifulSoup(str1, "html.parser")
#soup = BeautifulSoup(str1,'html5lib') 
soup = BeautifulSoup(str1,'lxml') 
#print (soup.prettify('utf-8'))
f = open("ttjiexml.txt"  , "w" , encoding = 'utf-8'  , errors='ignore')
ss = soup.prettify('utf-8')
mm = str(ss,'utf-8')
f.write( mm )
f.close() 
#print(ss)
#print(soup.title)  #获取标题
#print(soup.title.text)  #标题明称
#print(soup.title.text)  
#print(soup.body)  
items = soup.find_all("img" ,file = re.compile("jpg") )  
for link in items:
    print( link )
    #print(link.get('alt'))
    print(link.get('file')) 	
   # print(link.get('src'))  
#print(soup.get_text()) 	

items = soup.find_all("a" ,href = re.compile("txt") )  
for link in items:
    print(link.get('href')) 
