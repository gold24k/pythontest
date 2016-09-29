# -*- coding: utf-8 -*-
import urllib  
import urllib2
import cookielib

cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#需要POST的数据#
postdata=urllib.urlencode({  
    'log':'ksboy17',  
    'pwd':'wyh@wsx17'  
})

#自定义一个请求#
req = urllib2.Request(  
    url = 'http://fulisoso.net/wp-login.php/',  
    data = postdata
)

#访问该链接#
result = opener.open(req)

#打印返回的内容#
print result.read() 
