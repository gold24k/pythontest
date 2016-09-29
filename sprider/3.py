import urllib.request as request  
  
if __name__ == '__main__':  
    response = request.urlopen("http://www.sina.com.cn")  
    data = response.read()  
  #  print(type(data))       # <class 'bytes'>  
  #  print(data)             #输出字节码内容  
    print(str(data,encoding = "utf-8")) #将字节码转换成utf-8编码的字符串  
