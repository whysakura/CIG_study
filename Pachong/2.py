from urllib import request, parse
import re


class Tool(object):
    removing = r'<img.*?>|\s{7}'
    replacing = r'<br>'
    replace_a = r'<a.*?</a>'

    def __init__(self):
        print('导入成功')

    def replace(self, x):
        x = re.sub(self.removing, '', x)
        x = re.sub(self.replacing, '\n', x)
        x = re.sub(self.replace_a, '', x)
        return (x.strip())


class BDTB(object):
    def __init__(self):
        self.page = 1
        self.headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0',
                        'Connection': 'keep-alive',
                        }
        self.data = None
        self.datalist = []
        self.apage = None
        self.hui = None
        self.tool = Tool()
        self.allpage()

    def getdata(self, page):
        try:
            self.url = 'http://tieba.baidu.com/p/3138733512?pn=%d' % (page)
            req = request.Request(self.url, headers=self.headers)
            f = request.urlopen(req)
            data = f.read().decode('utf-8')
            self.data = data
            return data
        except:
            print('error')

    def select_data(self, id):
        a = re.findall(r'class="l_post l_post_bright j_l_post clearfix'
                       r'.*?name&quot;:&quot;(.*?)&quot;,.*?post_index&quot;:(.*?),'
                       r'.*?d_author">.*?class="(.*?)">.*?'
                       r'd_post_content j_.*?>(.*?)</div>', self.data, re.S)
        if id == 1:
            for i in a:
                if i[2] == 'louzhubiaoshi_wrap':
                    te = self.tool.replace(i[3])
                    self.datalist.append([i[0], i[1], i[2], te])
        if id == 2:
            for i in a:
                te = self.tool.replace(i[3])
                self.datalist.append([i[0], i[1], i[2], te])

    def allpage(self):
        self.getdata(self.page)
        d = re.findall(r'<li class="l_reply_num" style="margin-left:8px" >.*?3px">(.*?)<.*?'
                       r'red">(.*?)<.*?</li>', self.data, re.S)
        self.apage = d[0][1]
        self.hui = d[0][0]
        print(self.apage, self.hui)
        return ()

    def write(self):
        for i in self.datalist:
            with open('aaa.txt', 'a') as f:
                l = f.tell()
                f.write('\n姓名：{0}\n-------------------{1}楼-------------------------------\n内容：{2}\n'.format(
                    i[0].encode('utf-8').decode('unicode_escape'), i[1],
                    i[3]))
                print(l, ':写入成功')
                f.close()

    def start(self, id):
        for i in range(1, int(self.apage) + 1):
            self.getdata(i)
            self.select_data(id)
            self.write()
            print('正在写入', i, '....')
            # print(self.datalist)
            input('')


bd = BDTB()
# bd.select_data(1, 1)
bd.start(2)
# print(bd.data)
# a = '\\u62bd\\u652f\\u5929\\u4e0b\\u79c0'
# b=u'寂杀哲理'
# print(a.encode('utf-8').decode('unicode_escape'))
# print(b.encode())
