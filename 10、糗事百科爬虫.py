import urllib.request
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')



def jokeCrawler(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    }

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'

    re_joke = re.compile(pat,re.S)
    divsList = re_joke.findall(HTML)
    #print(divsList)
    #print(len(divsList))

    dic = {}
    for div in divsList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)
        username = username[0]

        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]

        dic[username] = duanzi

    return dic
   # with open(r"D:\pythonProject\34、爬虫\file3.html","w") as f:
      #   f.write(HTML)


url = "https://www.qiushibaike.com/text/"
info = jokeCrawler(url)

for k,v in info.items():
    print(k,v)


