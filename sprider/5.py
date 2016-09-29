# -*-coding:utf-8 -*- 
import httplib2  #######可以正常抓取页面
import urllib
import urllib.request
import chardet  #用于获取当前页面的编码格式函数
import re #正则表达式模块  
import io 
import sys
import gzip
def loadData(url,headers):
	request = urllib.request.Request(url=url, headers=headers )
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
url='http://www2.beareyes.com.cn/bbs/1.htm'
#content = http.request(url,'GET')  
#type = sys.getfilesystemencoding()# win下大多为mbcs 无法使用
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
'Chrome/51.0.2704.63 Safari/537.36'}  
con = loadData(url,headers)
chardit1 = chardet.detect(con) #格式为{'confidence': 0.99, 'encoding': 'utf-8'}
print (chardit1)
#print(str(con, "GB2312"))
#使用ignore 可以在出现转码错误时进行忽略
f = open("tt.txt"  , "w" , encoding = chardit1["encoding"]  , errors='ignore')
#print(type)
f.write(str(con,chardit1["encoding"], errors='ignore')) 
f.close() 
print("write down")
#print(con)
