'''
Function:
    小说下载器
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import sys
import time
import copy
import json
import click
import threading
if __name__ == '__main__':
    from modules import *
    from __init__ import __version__
else:
    from .modules import *
    from .__init__ import __version__


'''basic info'''
BASICINFO = '''************************************************************
Function: 小说下载器 V%s
Author: Charles
微信公众号: Charles的皮卡丘
操作帮助:
    输入r: 重新初始化程序(即返回主菜单)
    输入q: 退出程序
    下载多部小说: 选择想要下载的小说时,输入{1,2,5}可同时下载第1,2,5部小说
小说保存路径:
    当前路径下的%s文件夹内
************************************************************'''


'''小说下载器'''
class noveldl():
    def __init__(self, configpath=None, config=None, **kwargs):
        assert configpath or config, 'configpath or config should be given'
        self.config = loadconfig(configpath) if config is None else config
        self.initializeAllSources()
    '''运行'''
    def run(self, target_srcs=None):
        while True:
            print(BASICINFO % (__version__, self.config.get('savedir')))
            # 输入关键字
            user_input = self.dealInput('请输入小说搜索的关键词: ')
            # 搜索小说并打印搜索结果
            target_srcs = ['zw81', 'gebiqu', 'xbiquge'] if target_srcs is None else target_srcs
            search_results = self.search(user_input, target_srcs)
            title = ['序号', '作者', '小说名', '来源']
            items, records, idx = [], {}, 0
            for key, values in search_results.items():
                for value in values:
                    items.append([str(idx), value['author'], value['title'], value['source'].upper()])
                    records.update({str(idx): value})
                    idx += 1
            printTable(title, items)
            # 小说下载
            user_input = self.dealInput('请输入想要下载的小说编号: ')
            need_download_numbers = user_input.replace(' ', '').split(',')
            novel_infos = []
            for item in need_download_numbers:
                novel_info = records.get(item, '')
                if novel_info: novel_infos.append(novel_info)
            self.download(novel_infos)
    '''小说搜索'''
    def search(self, keyword, target_srcs):
        self.logging(f'正在搜索 {keyword} 来自 {" | ".join([c.upper() for c in target_srcs])}')
        def threadSearch(search_api, keyword, target_src, search_results):
            try:
                search_results.update({target_src: search_api(keyword)})
            except Exception as err:
                self.logging('无法在%s中搜索 >>>> %s' % (target_src, keyword))
        task_pool, search_results = [], {}
        for target_src in target_srcs:
            task = threading.Thread(
                target=threadSearch,
                args=(getattr(self, target_src).search, keyword, target_src, search_results)
            )
            task_pool.append(task)
            task.start()
        for task in task_pool:
            task.join()
        return search_results
    '''小说下载'''
    def download(self, novel_infos):
        for novel_info in novel_infos:
            getattr(self, novel_info['source']).download([novel_info])
    '''初始化所有支持的搜索/下载源'''
    def initializeAllSources(self):
        supported_sources = {
            'zw81': Zw81Novel, 'gebiqu': GeBiquNovel, 'xbiquge': XbiqugeNovel
        }
        for key, value in supported_sources.items():
            setattr(self, key, value(copy.deepcopy(self.config), self.logging))
        return supported_sources
    '''处理用户输入'''
    def dealInput(self, tip=''):
        user_input = input(tip)
        if user_input.lower() == 'q':
            self.logging('ByeBye')
            sys.exit()
        elif user_input.lower() == 'r':
            self.initializeAllSources()
            self.run()
        else:
            return user_input
    '''logging'''
    def logging(self, msg, tip='INFO'):
        print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {tip}]: {msg}')
    '''str'''
    def __str__(self):
        return 'Welcome to use noveldl!\nYou can visit https://github.com/CharlesPikachu/noveldl for more details.'


'''cmd直接运行'''
@click.command()
@click.version_option()
@click.option('-k', '--keyword', default=None, help='想要搜索下载的小说关键字, 若不指定, 则进入noveldl终端版')
@click.option('-p', '--proxies', default='{}', help='设置的代理')
@click.option('-s', '--savedir', default='novels', help='下载的小说的保存路径')
@click.option('-c', '--count', default='5', help='在各个平台搜索时的小说搜索数量')
@click.option('-t', '--targets', default='zw81,gebiqu', help='指定小说搜索下载的平台, 例如"zw81,gebiqu"')
def noveldlcmd(keyword, proxies, savedir, count, targets):
    config = {
        'proxies': json.loads(proxies),
        'savedir': savedir,
        'search_size_per_source': int(count),
    }
    target_srcs = [
        'zw81', 'gebiqu', 'xbiquge'
    ] if targets is None else [src.strip() for src in targets.split(',')]
    dl_client = noveldl(config=config)
    if keyword is None:
        dl_client.run(target_srcs=target_srcs)
    else:
        print(dl_client)
        search_results = dl_client.search(keyword, target_srcs)
        # 打印搜索结果
        title = ['序号', '作者', '小说名', '来源']
        items, records, idx = [], {}, 0
        for key, values in search_results.items():
            for value in values:
                items.append([str(idx), value['author'], value['title'], value['source'].upper()])
                records.update({str(idx): value})
                idx += 1
        printTable(title, items)
        # 小说下载
        user_input = dl_client.dealInput('请输入想要下载的小说编号: ')
        need_download_numbers = user_input.replace(' ', '').split(',')
        novel_infos = []
        for item in need_download_numbers:
            novel_info = records.get(item, '')
            if novel_info: novel_infos.append(novel_info)
        dl_client.download(novel_infos)


'''run'''
if __name__ == '__main__':
    dl_client = noveldl('config.json')
    dl_client.run()