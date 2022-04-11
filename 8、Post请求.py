'''
特点：把参数进行打包，单独传输

优点：数量大，安全（当对服务器数据进行修改时建议使用post）

缺点：速度慢

'''

import urllib.request
import urllib.parse

url = "http://www.sunck.wang:8085/form"
#将要发送的数据合成一个字典
#字典的键值网址里找，一般为input标签的name属性的值
data = {
    "username":"sunck",
    "passwd":"666"
}

#对要发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url,postData)
#请求
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))








