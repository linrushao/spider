import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r"D:\pythonProject\34、爬虫\file2.html")

#urlretrieve在执行的过程中，会产生一些缓存
#清除缓存
urllib.request.urlcleanup()




















