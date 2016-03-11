# -------爬虫一之糗事百科
from urllib import parse, request
import re, time


class QSBK(object):
    def __init__(self):
        self.data = []
        self.infopage = 1
        self.enable = True

    def read(self, infopage):
        try:
            re = request.Request('http://www.qiushibaike.com/hot/page/{0}/?s=4856558/'.format(infopage))
            re.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0')
            f = request.urlopen(re)
            print(f.status, f.reason)
            res = f.read().decode('utf-8')
            return (res)
        except:
            print('Error:')

    def getdata(self, infopage):
        if not infopage:
            print('jia zai shi bai !')
            return
        d = self.read(infopage)
        data = re.findall(r'<div class="author clearfix">.*?<img.*?/>.*?'
                          r'<h2>(.*?)</h2>.*?<div class="content">'
                          r'\s+(.*?)\s+<!--(.*?)-->.*?</div>'
                          r'.*?<div class="(.*?)".*?<i class="number">(.*?)</i>', d, re.S)
        for i in data:
            if not i[3] == 'thumb':
                text = re.sub(r'<br/>', '\r\n', i[1])
                self.data.append([i[0], text, time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(int(i[2]))), i[4]])
        # print(self.data)
        # self.data=[self.data[i] for i in range(len(self.data)) if self.data[i] not in self.data[:i]]
        # print('-----------------')-------------------------------------------------
        # print(self.data)
        return

    def getpage(self):
        if len(self.data) == 0:
            self.infopage += 1
            self.getdata(self.infopage)
        for i in self.data:
            print(len(self.data))
            print('姓名：{0}\r\n内容：{1}\r\n时间：{2}\r\n点赞:{3}'.format(*i))
            self.data.remove(i)
            ii = input()
            if ii == 'q':
                self.enable = False
                break

        return

    def start(self):
        self.getdata(self.infopage)
        while self.enable:
            self.getpage()


cl = QSBK()
cl.start()
