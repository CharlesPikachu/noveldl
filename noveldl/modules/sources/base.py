'''
Function:
    小说搜索下载基类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import requests
from ..utils import Downloader


'''小说搜索下载基类'''
class BaseNovel():
    def __init__(self, config, logger_handle):
        self.config = config
        self.logger_handle = logger_handle
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.proxies.update(config['proxies'])
    '''搜索'''
    def search(self, keyword):
        raise NotImplementedError('not to be implemented')
    '''下载'''
    def download(self, novel_infos):
        for novel_info in novel_infos:
            novel_info = self.parse(novel_info)
            self.logger_handle('正在从%s下载 >>>> %s' % (self.source.upper(), novel_info['title']))
            task = Downloader(novel_info, self.session)
            if ('chapters' in novel_info) and task.start():
                self.logger_handle('成功从%s下载到了 >>>> %s' % (self.source.upper(), novel_info['title']))
            else:
                self.logger_handle('无法从%s下载 >>>> %s' % (self.source.upper(), novel_info['title']))
    '''解析小说信息'''
    def parse(self):
        raise NotImplementedError('not to be implemented')