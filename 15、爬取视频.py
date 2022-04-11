import time
import urllib.request
import re
import os
import requests



def imageCrawler(url,topath):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    }

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")

    #with open(r"D:\pythonProject\34、爬虫\image2\yhd.html","wb") as f:
     #   f.write(HtmlStr)
    #正则表达式
    pat = r'data-url="(.*?).mp4" class="fr">点击播放</a>'

    re_image = re.compile(pat,re.S)
    imagesList = re_image.findall(HtmlStr)

    #print(imagesList)
    #print(len(imagesList))
    #print(imagesList[4])


    for imageUrl in imagesList:
        path = os.path.join(topath,imageUrl.split("：")[-1]+".mp4")
        video_data = imageUrl + ".mp4"
        video = requests.get(url=video_data, headers=headers).content
        #把图片下载到本地存储
        with open(path,"wb")as f:
            f.write(video)
        print("%s--下载成功！!"%imageUrl.split("：")[-1])
    time.sleep(1)

#http://video.mobiletrain.org/course/index/courseId/401
url = "http://video.mobiletrain.org/course/index/courseId/401"
topath = r"D:\PythonCrawler\image2"
imageCrawler(url,topath)












