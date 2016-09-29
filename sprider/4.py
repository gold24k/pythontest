# -*-coding:utf-8 -*- 
import httplib2  #######可以正常抓取页面
import urllib
import urllib.request
import re #正则表达式模块  
import io 
import sys
import gzip
def loadData(url):
	request = urllib.request.Request(url)
	request.add_header('Accept-encoding', 'gzip')
	response = urllib.request.urlopen(request)
	if response.info().get('Content-Encoding') == 'gzip':
		print ('gzip enabled')
		buf = io.BytesIO (response.read())
		f = gzip.GzipFile(fileobj = buf)
		data = f.read()
		
	else:
		data = response.read()
	return data
	
#http = httplib2.Http() 
#headers={"cookie":''}      
url='http://www.sina.com.cn'
#content = http.request(url,'GET')  
type = sys.getfilesystemencoding()
con = loadData(url)
print(str(con, "utf-8"))

f = open("tt.txt"  , "w" , encoding= 'utf-8')
print(type)
f.write(str(con, "utf-8")) 
f.close() 
print("write down")
#print(con)
