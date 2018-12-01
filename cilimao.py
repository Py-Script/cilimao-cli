# coding: utf-8

"""命令行磁力猫查询
默认选择按视频排序,按下载热度排序

Usage:
    cilimao [-p] <KEYWORD>
    cilimao [-h,--help]   显示帮助菜单

Options:
    -h,--help       显示帮助菜单
    -p              页数(默认为0)   

Example:
    cilimao 复仇者联盟
    cilimao -p 1 复仇者联盟
"""
import requests
from docopt import docopt

class Parase:

    def __init__(self, result):
        self.result = result

    
    def parase_a(self):
        """
        解析数据
        result: 传入待解析的数据
        """
        try:
            leng = str(self.result['content_size'])
            if len(leng) <= 9:
                size = int(leng) / 1048576
                sizeS = str(size) + 'MB'
            elif len(leng) >= 10:
                size = int(leng) / 1073741824
                sizeS = str(size) + 'GB'
            infohash = self.result['infohash']
            title = self.result['title']
            file_count = self.result['file_count']
            cre_time = self.result['created_time']

            print('磁链标题: ', title)
            print('磁链地址: magnet:?xt=urn:btih:{}'.format(infohash))
            print('文件数目: ', file_count)
            print('文件大小: ', sizeS)
            print('创建时间: ', cre_time , '\n')
        except Exception as e:
            print('磁链标题: ', title)
            print('磁链地址: magnet:?xt=urn:btih:{}'.format(infohash))
            print('文件数目: ', file_count)
            print('文件大小: ', sizeS)
            print('创建时间: ', cre_time , '\n')
            print('Error Ex', e, '\n')



def run():
    """程序入口"""
    arguments = docopt(__doc__)
    keyword = arguments['<KEYWORD>']
    if arguments['-p'] is True:
        page = arguments['-p']
    else:
        page = 0
    
    url = ('https://www.cilimao.me/api/search?size=10&'
           'sortDirections=desc&word={}&'
           'sortProperties=download_countpage={}').format(
            keyword, page)
    r = requests.get(url)
    print('Crawling data for you.....')
    result = r.json()['data']['result']['content']
    for item in result:
        if 'infohash' in item:
            Parase(item).parase_a()

if __name__ == "__main__":
    run()
