# -*-coding:utf-8 -*- 
import httplib2  #######改用httplib2进行抓取数据增加cookie
import urllib
import urllib.request
import chardet  #用于获取当前页面的编码格式函数
import re #正则表达式模块  
import io 
import sys
import gzip
import bs4
from bs4 import BeautifulSoup  
def loadData(url,headers):
    http = httplib2.Http( timeout=2 )  
    response,content = http.request( url,'GET',headers = headers )
    #print(response)  #此处可以判断获取的各种状态信息
    #print(response['-content-encoding'])
    return content
	######暂时注销掉使用gzip的格式 因为httplib2 可以自动解压缩网页文件所以不用压缩
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
#headers={"cookie":'Cookie: a4203_times=4; wordpress_logged_in_5161d1aeb159caad7f82805bbea717ab=ksboy117%7C1472094140%7Cp7w83hY21oCXveKLLwH4MQ7QNBzgsOCiSEMwCJIQ212%7C6f99fdfc41b8df5ab1d29d9e50cacf9570b6c925d48bfe5aa8a24bdba8dcd315; a4203_pages=2; dx_current_page=http%3A//fulisoso.net/; wordpress_test_cookie=WP+Cookie+check'}  
headers = {"cookie":'Cookie: TIEBA_USERTYPE=ae4849f4a4cebc4a5540be7d; TIEBAUID=c5f54a97a9c64a2e28161dfb; bdshare_firstime=1464939463762; wise_device=0; LONGID=671473093; BAIDUID=D59561E618C5F911EB50C9B1DDDF690D:FG=1; BIDUPSID=D59561E618C5F911EB50C9B1DDDF690D; PSTM=1464852613; __cfduid=dd66bf852eb4cb3ffef38ee3f9cbc3a981470707867; BDUSS=216QzZLY0Z4TzVGU3E3dzJYQ3VxUn5jNFVSdnpkU0Y0b0RMYkJvMkdYUWJhZE5YQVFBQUFBJCQAAAAAAAAAAAEAAADF3QUoZ2-~ycDWvKaz4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABvcq1cb3KtXV; BDRCVFR[k2U9xfnuVt6]=mk3SLVN4HKm; H_PS_PSSID=1452_18240_19861_17001_12108_20645_20770_20719; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0'}
#url='http://fulisoso.net/?p=45330'
url = 'http://www.baidu.com'
#content = http.request(url,'GET')  
#type = sys.getfilesystemencoding()# win下大多为mbcs 无法使用
con = loadData(url,headers)
chardit1 = chardet.detect(con) #格式为{'confidence': 0.99, 'encoding': 'utf-8'}
#print (chardit1)
#print(str(con, "GB2312"))
#使用ignore 可以在出现转码错误时进行忽略
f = open("tt.html"  , "w" , encoding = chardit1['encoding']  , errors='ignore')
#print(type)
ss = str(con,chardit1['encoding'], errors='ignore')
f.write(ss) 
f.close() 
print("write down")
#print(con)

 
