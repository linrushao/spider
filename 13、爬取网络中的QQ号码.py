import urllib.request
import ssl
import re
import os
from collections import deque

def writeFileBytes(htmlBytes,topath):
    with open(topath,"wb") as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,topath):
    with open(topath,"w") as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()

def qqCrawler(url,topath):
    htmlBytes = getHtmlBytes(url)
    #writeFileBytes(htmlBytes,r"D:\pythonProject\34、爬虫\爬取QQ\File1.html")
    #writeFileStr(htmlBytes,r"D:\pythonProject\34、爬虫\爬取QQ\File2.txt")

    htmlStr = str(htmlBytes)

    '''
    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqList = re_qq.findall(htmlStr)
    #去重
    qqList = list(set(qqList))
    print(qqList)
    print(len(qqList))
    '''

    #匹配网址
    pat = r'((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?'

    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    # 去重
    qqsList = list(set(urlsList))
    #print(urlsList)
    #print(len(urlsList))

    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重
    qqsList = list(set(qqsList))
    f = open(topath,"a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
    f.close()

    return urlsList

#qqCrawwler(url,topath)

def center(url,topath):
    queue =deque()

    queue.append(url)

    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl,topath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = r"https://tieba.baidu.com/p/421767762?red_tag=1236252029"

topath = r"D:\PythonCrawler\qqFile.txt"
try:
    center(url,topath)
except:
    pass







