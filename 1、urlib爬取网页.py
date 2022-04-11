import urllib.request

#向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")

#读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
#data = response.read()
#print(data)
#print(type(data))

#读取一行，要写循环
#data = response.readline()


#读取文件的全部内容，会把读取到的数据赋值给一个列表变量
data = response.readlines()

#print(data)
#print(type(data))
#print(len(data))
#每一个元素的类型
#print(type(data[100].decode("utf-8")))




#将爬取到的网页写入文件
#with open(r"D:\pythonProject\34、爬虫\file1.html","wb") as f:
#    f.write(data)

#response  属性
#返回环境的有关信息
print(response.info())

#返回状态码
print(response.getcode())
#if response.getcode() == 200 or response.getcode()  == 304:
    #处理网页信息
 #   pass

#返回当前正在爬取的URL地址
print(response.geturl())


url = "http://139.9.125.73:8007/"
#解码
newUrl = urllib.request.unquote(url)
print(newUrl)
#编码

newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)

