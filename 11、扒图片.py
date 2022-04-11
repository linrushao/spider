import urllib.request
import re
import os


def imageCrawler(url,topath):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    }

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("gbk")

   # with open(r"D:\pythonProject\34、爬虫\image\yhd.html","wb") as f:
     #   f.write(HtmlStr)
    #正则表达式
    pat = r'<img src="(.*?)" alt="(.*?)" />'
    re_image = re.compile(pat,re.S)
    imagesList = re_image.findall(HtmlStr)

    #print(imagesList)
    #print(len(imagesList))
    #print(imagesList[4])


    num = 1
    for imageUrl in imagesList:
        path = os.path.join(topath,str(num)+".jpg")
        num +=1
        #把图片下载到本地存储
        urllib.request.urlretrieve("https://pic.netbian.com"+imageUrl[0],filename=path)

try:
    url = "https://pic.netbian.com/4kmingxing/"
    topath = r"D:\PythonCrawler\image"
    imageCrawler(url,topath)
except:
    pass











