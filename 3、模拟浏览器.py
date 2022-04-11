import urllib.request
import random


url = "http://www.baidu.com"

'''
#模拟请求头
#完整的请求头
headers = {
    "Accept":"application/json,text/javascript,*/*;q=0.01",
    "X-Requested-with":"XMLHttpRequest",
    "Uers--Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"
    "Content-Type":"application/x-www-from-urlencoded;charset=UTF-8"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
'''


agentsList = [
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加了User--Agent
req.add_header("User--Agent",agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

