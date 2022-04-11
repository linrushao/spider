'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为起量级的传输方式

json文件组成
{}      代表对象（字典）
[]      代表列表
:       代表键值对
,       分隔两个部分
'''
import json

jsonStr = '{"name":"linrs","age":18,"hobby":["money","power","math"],"parames":{"a":1,"b":2}}'

#将json格式的字符串转为python数据类型的对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])

#将python数据类型的对象转为son格式的字符串

jsonData2 = '{"name":"linrs","age":18,"hobby":["money","power","math"],"parames":{"a":1,"b":2}}'
jsonStr = json.dumps(jsonData2)
print(jsonStr)
print(type(jsonStr))


#写本地json

path = r"D:\pythonProject\34、爬虫\test.json"
jsonData3 = {"name":"linrs","age":18,"hobby":["money","power","math"],"parames":{"a":1,"b":2}}
with open(path,"w") as f:
    json.dump(jsonData3,f)

#读取本地的json文件
path2 = r"D:\pythonProject\34、爬虫\test.json"
with open(path,"rb") as f:
    data = json.load(f)
    print(data)
    #字典类型
    print(type(data))




