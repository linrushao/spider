import urllib.request
import ssl
import json



def ajaxCrawler(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    }

    req = urllib.request.Request(url,headers=headers)

    #使用ssl创建未验证的上下文  可以访问https网页
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)


    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData

'''
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)
print(info)
'''

for i in range(1,11):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i*20)+"&limit=20"
    info = ajaxCrawler(url)
    print(len(info))


