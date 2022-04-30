'''
Function:
    从www.gebiqu.com搜索和下载小说
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import re
from lxml import etree
from .base import BaseNovel
from ..utils import filterBadCharacter


'''从www.gebiqu.com搜索和下载小说'''
class GeBiquNovel(BaseNovel):
    def __init__(self, config=None, logger_handle=None):
        super(GeBiquNovel, self).__init__(config=config, logger_handle=logger_handle)
        self.source = 'gebiqu'
        self.search_url = 'https://www.gebiqu.com/modules/article/search.php?searchkey={}'
    '''搜索'''
    def search(self, keyword):
        # 发送请求
        search_url = self.search_url.format(keyword)
        html = etree.HTML(self.session.get(search_url).content.decode('utf-8'))
        # 整理结果
        novel_infos = []
        titles = html.xpath('//*[@id="nr"]/td[1]/a/text()')
        authors = html.xpath('//*[@id="nr"]/td[3]/text()')
        download_urls = html.xpath('//*[@id="nr"]/td[2]/a/@href')
        for idx in range(len(authors)):
            title = filterBadCharacter(titles[idx])
            author = filterBadCharacter(authors[idx])
            download_url = re.sub(r'\d*.html$', '', str(download_urls[idx]))
            novel_infos.append({
                'source': self.source,
                'title': title,
                'author': author,
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
        html = etree.HTML(response.content.decode('utf-8'))
        # 获得书本的基础信息
        title = html.xpath('//*[@id="info"]/h1/text()')[0]
        author = html.xpath('//*[@id="info"]/p[1]/text()')[0].split('：')[1]
        image_url = html.xpath('//*[@id="fmimg"]/img/@src')[0]
        introduction = html.xpath('//*[@id="intro"]/p/text()')[0]
        chapter_names_list = html.xpath('//*[@id="list"]/dl/dt[2]//following-sibling::*/a/text()')
        chapter_urls_list = html.xpath('//*[@id="list"]/dl/dt[2]//following-sibling::*/a/@href')
        # 解析所有章节
        chapters = []
        for idx in range(len(chapter_names_list)):
            chapters.append({
                'title': filterBadCharacter(chapter_names_list[idx]),
                'download_url': 'http://www.gebiqu.com' + chapter_urls_list[idx]
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