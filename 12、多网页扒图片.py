import time
import urllib.request
import re
import os
import ssl



def imageCrawler(url,topath):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    req = urllib.request.Request(url,headers=headers)
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    HtmlStr = response.read().decode("gbk")
    pat = r'<img src="/uploads/allimg/(.*?)" alt="(.*?)" />'
    re_image = re.compile(pat,re.S)
    imagesList = re_image.findall(HtmlStr)
    #print(imagesList)

    #num = 1
    for imageUrl in imagesList:
        path = os.path.join(topath,imageUrl[1]+".jpg")
        #num +=1
        #把图片下载到本地存储
        urllib.request.urlretrieve("https://pic.netbian.com/uploads/allimg/"+imageUrl[0],filename=path)


topath = r"D:\PythonCrawler\image"
for i in range(2,10):
    url = "https://pic.netbian.com/4kmingxing/index_"+str(i)+".html"
    time.sleep(2)
    #print(url)
    imageCrawler(url, topath)

