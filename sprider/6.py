# -*-coding:utf-8 -*- 
import httplib2  #######改用httplib2进行抓取数据增加cookie
import urllib
import urllib.request
import chardet  #用于获取当前页面的编码格式函数
import re #正则表达式模块  
import io 
import sys
import gzip
def loadData(url,headers):
    http = httplib2.Http()  
    response,content = http.request( url,'GET',headers=headers)
    return content
	######暂时注销掉使用gzip的格式
	# request = urllib.request.Request(url)
	# request.add_header('Accept-encoding', 'gzip')
	# response = urllib.request.urlopen(request)
    
    # if content.info().get('Content-Encoding') == 'gzip':
    # print ('gzip enabled')
        # buf = io.BytesIO (content.read())
        # f = gzip.GzipFile(fileobj = buf)
        # data = f.read()
		
	# else:
    # data = content.read()
    # return data
	
#http = httplib2.Http() 
headers={"cookie":'Cookie: a4203_times=4; wordpress_logged_in_5161d1aeb159caad7f82805bbea717ab=ksboy117%7C1472094140%7Cp7w83hY21oCXveKLLwH4MQ7QNBzgsOCiSEMwCJIQ212%7C6f99fdfc41b8df5ab1d29d9e50cacf9570b6c925d48bfe5aa8a24bdba8dcd315; a4203_pages=2; dx_current_page=http%3A//fulisoso.net/; wordpress_test_cookie=WP+Cookie+check'}  
    
url='http://fulisoso.net/'
#content = http.request(url,'GET')  
#type = sys.getfilesystemencoding()# win下大多为mbcs 无法使用
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
