'''
Function:
    下载器类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import time
import random
import requests
from lxml import etree
from .ua import randomua
from .misc import touchdir
from alive_progress import alive_bar


'''下载器类'''
class Downloader():
    def __init__(self, novel_info, session=None, logger_handle=None, **kwargs):
        self.novel_info = novel_info
        self.session = requests.Session() if session is None else session
        self.logger_handle = logger_handle
        self.__setheaders(novel_info['source'])
    '''外部调用'''
    def start(self):
        # 初始化
        novel_info, session, headers = self.novel_info, self.session, self.headers
        touchdir(novel_info['savedir'])
        savedir = os.path.join(novel_info['savedir'], novel_info['title'])
        touchdir(savedir)
        # 开始下载
        with alive_bar(manual=True) as bar:
            for chapter_idx, chapter in enumerate(novel_info['chapters']):
                for _ in range(10):
                    response = self.session.get(chapter['download_url'], headers=self.headers)
                    if response.status_code == 200: break
                    self.headers['User-Agent'] = randomua()
                    time.sleep(random.random())
                if response.status_code != 200: 
                    self.logger_handle(f"无法下载章节 >>>> {chapter['title']}, 章节链接 >>>> {chapter['download_url']}")
                    continue
                html = etree.HTML(response.content.decode('utf-8'))
                lines = html.xpath('//div[@id="content"]/text()')
                for line_idx, content in enumerate(lines):
                    content = content.replace(u'\x20', u'\n')
                    content = content.replace(u'\xa0', u'')
                    content = content.replace(u'\u3000', ' ')
                    lines[line_idx] = content
                content = '\n'.join(lines)
                fp = open(os.path.join(savedir, f'{chapter["title"]}.txt'), 'w', encoding='utf-8')
                fp.write(content)
                fp.close()
                bar.text(chapter['title'])
                bar(min((chapter_idx + 1) / len(novel_info['chapters']), 1))
        return True
    '''设置请求头'''
    def __setheaders(self, source):
        if hasattr(self, f'{source}_headers'):
            self.headers = getattr(self, f'{source}_headers')
        else:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            }