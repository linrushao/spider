
'''
http: // 7
xtcwd.com1.z0.glb.clouddn.com / 千锋Java教程：_44_封装.mp4
'''

import time
import urllib.request
import re
import os
import requests

url1 = "https://movie.douban.com/subject/35231370/comments?limit=20&status=F&sort=new_score"
url2 = 'https://movie.douban.com/subject/35231370/comments?start=20&limit=20&status=F&sort=new_score'

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Cookie: ll="118281"; bid=kupwb9gjMII; _vwo_uuid_v2=D56A40B679523355B5C2F048F876BC889|e8217eeb8122873ade257dbfabb3de50; ct=y; __gads=ID=0241990103903bfb-2224551d88cb00ff:T=1630724162:RT=1630724162:S=ALNI_MY-Tigaw9Q5a83Dm6qaKtZRYGjMow; __yadk_uid=0qJMks7uXHfkA6PViJRehcoOUDE5AQvd; douban-fav-remind=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1631802964%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DUJWmeOgL8h8HTf7z172VJYKrnrY5b4UqUwpNm8BxQriZrXKVut9QcfrTuzp0_7O-%26wd%3D%26eqid%3Dcee64e34000000b50000000661435652%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1402186321.1630724142.1631581549.1631802964.3; __utmb=30149280.0.10.1631802964; __utmc=30149280; __utmz=30149280.1631802964.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.265268074.1630724147.1630724147.1631802964.2; __utmb=223695111.0.10.1631802964; __utmc=223695111; __utmz=223695111.1631802964.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; _pk_id.100001.4cf6=02a6273ded3349bc.1630724147.2.1631803041.1630724258.
Host: movie.douban.com
Referer: https://movie.douban.com/subject/35231370/
sec-ch-ua: "Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47




haeders =


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
    #pat = r'http: // 7xtcwd.com1.z0.glb.clouddn.com / 千锋Java教程：_44_封装.mp4'

    #re_image = re.compile(pat,re.S)
    #imagesList = re_image.findall(HtmlStr)

    #print(imagesList)
    #print(len(imagesList))
    #print(imagesList[4])

    '''
    for imageUrl in imagesList:
        path = os.path.join(topath,imageUrl.split("：")[-1]+".mp4")
        video_data = imageUrl + ".mp4"
    '''
    h = 'http: // 7xtcwd.com1.z0.glb.clouddn.com / 千锋Java教程：_44_封装.mp4'
    video = requests.get(url=h, headers=headers).content
    #把图片下载到本地存储
    with open(topath,"wb")as f:
        f.write(video)
    print("%s--下载成功！!")
    #time.sleep(1)

#http://video.mobiletrain.org/course/index/courseId/401

topath = r"D:\PythonCrawler\image2"
imageCrawler(url1,topath)












