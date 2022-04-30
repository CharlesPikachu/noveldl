'''
Function:
    从www.xbiquge.so搜索和下载小说
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
from lxml import etree
from .base import BaseNovel
from bs4 import BeautifulSoup
from urllib.parse import quote
from ..utils import filterBadCharacter


'''从www.xbiquge.so搜索和下载小说'''
class XbiqugeNovel(BaseNovel):
    def __init__(self, config=None, logger_handle=None):
        super(XbiqugeNovel, self).__init__(config=config, logger_handle=logger_handle)
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': "https://www.xbiquge.so/book/51730/"
        }
        self.session.headers.update(self.headers)
        self.source = 'xbiquge'
        self.search_url = 'https://www.xbiquge.so/modules/article/search.php?searchkey={}'
    '''搜索'''
    def search(self, keyword):
        # 发送请求
        search_url = self.search_url.format(quote(str.encode(keyword, 'GB2312')))
        response = self.session.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 整理结果
        novel_infos = []
        for item in soup.select('.novelslistss > li'):
            title = item.select_one('span:nth-child(2) > a:nth-child(1)').text.strip()
            author = item.select_one('span:nth-child(4)').text.strip()
            download_url = item.select_one('span:nth-child(2) > a:nth-child(1)').attrs['href']
            novel_infos.append({
                'source': self.source,
                'title': filterBadCharacter(title),
                'author': filterBadCharacter(author),
                'download_url': download_url,
            })
            if len(novel_infos) == self.config['search_size_per_source']: break
        # 返回结果
        return novel_infos
    '''解析小说信息'''
    def parse(self, novel_info):
        # 发送请求
        response = self.session.get(novel_info['download_url'])
        if response.status_code != 200: return novel_info
        html = etree.HTML(response.text)
        # 获得书本的基础信息
        title = html.xpath('/html/body/div[2]/div[2]/div[2]/h1')[0].text
        author = html.xpath('/html/body/div[2]/div[2]/div[2]/p[1]/a')[0].text
        image_url = html.xpath('/html/body/div[2]/div[2]/div[1]/img/@src')[0]
        introduction = ''.join(html.xpath('//*[@id="intro"]/text()')).replace('\xa0', '').replace(' ', '')
        chapter_names_list = list(set(html.xpath('//*[@id="list"]/dl/dt[1]//following-sibling::*/a/text()')))
        chapter_urls_list = list(set(html.xpath('//*[@id="list"]/dl/dt[1]//following-sibling::*/a/@href')))
        # 解析所有章节
        chapters = []
        for idx in range(len(chapter_names_list)):
            chapters.append({
                'title': filterBadCharacter(chapter_names_list[idx]),
                'download_url': novel_info['download_url'] + chapter_urls_list[idx],
            })
        # 返回结果
        novel_info = {
            'source': self.source,
            'title': filterBadCharacter(title),
            'author': filterBadCharacter(author),
            'image_url': image_url,
            'introduction': introduction,
            'chapters': chapters,
            'savedir': self.config['savedir'],
        }
        return novel_info