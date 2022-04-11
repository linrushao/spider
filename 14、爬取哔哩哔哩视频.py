import requests
from lxml import etree
import re
import os

if __name__ == '__main__':
    # 输入要爬取的内容
    content = input('请输入要爬取的内容:')
    # 输入爬取的页数
    pages = int(input('请输入爬取的页数：'))
    # 确认目标的url,设置if条件，进行判断
    for i in range(pages):
        if i == 0:
            url = f'https://search.bilibili.com/all?keyword={content}&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.17'
        else:
            url = f'https://search.bilibili.com/all?keyword={content}&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.17&page={i+1}'
        # 构造请求头参数
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Cookie':"_uuid=51132243-E3A9-C9B8-01F5-523B0341ECAB93346infoc; buvid3=4973D729-A785-490F-9F59-C697F3B17DE4143099infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|~Ru|~R|)0J'uY|mYmk||Y; PVID=1; bsource=search_baidu; finger=158939783; arrange=matrix; sid=79i15ujl"
        }
        # 发送请求，获取响应
        response_1 = requests.get(url,headers=headers)
        str_data = response_1.text
        # 数据为html文件，将html转换成py文件
        py_data = etree.HTML(str_data)
        # 提取视频页面对应的url列表
        url_list = py_data.xpath('//li[@class="video-item matrix"]/a[@target="_blank"]/@href')
        for i in url_list:
            # 由于url并不是完整的，因此需要拼接
            url_1 = 'https:' + i
            # 构造请求头参数
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'Cookie':"_uuid=51132243-E3A9-C9B8-01F5-523B0341ECAB93346infoc; buvid3=4973D729-A785-490F-9F59-C697F3B17DE4143099infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|~Ru|~R|)0J'uY|mYmk||Y; PVID=1; bsource=search_baidu; finger=158939783; sid=79i15ujl"
            }
            # 发送请求，获取响应
            response_2 = requests.get(url_1,headers=headers)
            # 数据为文本格式
            str_data1 =  response_2.text
            # 将数据转换成py格式的数据
            py_data1 = etree.HTML(str_data1)
            # 提取视频的名称
            title_ = py_data1.xpath('//title/text()')[0]
            # 对名称正则处理
            title_ = re.findall(r'(.*?)_哔哩哔哩',title_)[0]
            title_ = title_.replace('/','')
            # 提取纯视频和纯音频的url
            url_str = py_data1.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
            video_url = re.findall('"video":\[{"id":\d+,"baseUrl":"(.*?)",',url_str)[0]
            audio_url = re.findall('"audio":\[{"id":\d+,"baseUrl":"(.*?)",',url_str)[0]
            # 得到纯视频和纯音频的url后，构造新的请求头，发送请求
            headers_ = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'Referer':url_1
            }
            # 发送请求，获取响应,加上stream参数可以获取文件大小
            response_video = requests.get(video_url,headers=headers_,stream=True)
            response_audio = requests.get(audio_url,headers=headers_,stream=True)
            video_data = response_video.content
            audio_data = response_audio.content
            # 获取电影的大小,单位为kb
            audio_size = int(int(response_audio.headers['content-length'])/1024)
            video_size = int(int(response_video.headers['content-length'])/1024)
            # 将kb转化成MB
            audio_size1 = int(audio_size/1024)
            video_size1 = int(video_size/1024)
            # 避免名称重复，对名称进行处理
            title_new = title_+'!'
            # 保存数据
            with open(f'{title_new}.mp3','wb')as f:
                f.write(audio_data)
            print(f'{title_new}纯音频文件保存完毕...大小为：{audio_size}KB,{audio_size1}MB')
            with open(f'{title_new}.mp4','wb')as f:
                f.write(video_data)
            print(f'{title_new}纯音频文件保存完毕...大小为：{video_size}KB,{video_size1}MB')
            # 将纯音频和纯视频进行合成
            os.system(f'ffmpeg -i "{title_new}.mp3" -i "{title_new}.mp4" -c copy "{title_}.mp4" -loglevel quiet')
            # 打印合成后视频的大小
            res_size = int(os.stat(f'{title_}.mp4').st_size/1024)
            res_size1 = int(res_size/1024)
            print(f'{title_}视频文件合成后的大小为：{res_size}KB,{res_size1}MB')

            # 将纯视频和纯音频文件删除
            os.remove(f'{title_new}.mp3')
            os.remove(f'{title_new}.mp4')


            #<video crossorigin="anonymous" preload="auto" src="blob:https://www.bilibili.com/2e21827b-6403-4270-b122-0273c321fe2b"></video>
            #<video crossorigin="anonymous" preload="auto" src="blob:https://www.bilibili.com/91b8b944-0a9b-4ad1-80fc-ea32a2ab7eb2"></video>