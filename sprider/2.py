#-*-coding:UTF-8-*-，
import chardet 
import urllib2

  


response = urllib2.urlopen('http://www.sina.com.cn/')
html = response.read()
chardit1 = chardet.detect(html)
print (chardit1)
print (str(html) )



