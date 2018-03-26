# encoding: utf-8
import os
import pdfkit
import requests
from bs4 import BeautifulSoup


#link_file = '/Users/mingli/Downloads/5minutes/links'

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
#    'cookie': [
#        ('cookie-name1', 'cookie-value1'),
#        ('cookie-name2', 'cookie-value2'),
#    ],
    'no-outline': None
}

options = {
    'page-size': 'A4',  # Letter
    'minimum-font-size': 25,  ###
    # 'image-dpi':1500, ###

    'margin-top': '0.1in',  #0.75in
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': 'UTF-8',  #支持中文
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'outline-depth': 10,
}

def parse_url_to_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    body = soup.find_all(class_="rich_media_content")[0]
    html = str(body)
    tags=soup.findAll('img')
    for tag in tags:
        src = tag.get('data-src')
        if src:
            print src
    return html

def save_to_htmls(links):
    htmls = []
    for i,url in enumerate(links):
        html = parse_url_to_html(url)
        f_name = ".".join([str(i), "html"])
        print f_name
        with open(f_name, 'w') as f:
            f.write(html)
        htmls.append(f_name)
    print 'htmls:',htmls
    return htmls


def convert_pdf():
    links = ['http://mp.weixin.qq.com/s?__biz=MzIwMTM5MjUwMg==&amp;mid=2653587972&amp;idx=1&amp;sn=4ad5198dc29dd7ef3257247fdd674e5f&amp;chksm=8d30821dba470b0b6b55c1dd6fbf6cce6727346aad86e02194946fa5089f840507268df7a995&amp;scene=21#wechat_redirect', 'http://mp.weixin.qq.com/s?__biz=MzIwMTM5MjUwMg==&mid=2653587970&idx=1&sn=eeabd0d69d51a725b46a6fc773544773&chksm=8d30821bba470b0d03dbf113fb19564c82592bef0d168c3971341abdc72bd4e91c28d0e92d36&scene=21#wechat_redirect']
    htmls = save_to_htmls(links)
   # pdfkit.from_file(htmls, u'每天5分钟玩转 openstack.pdf', options=options)
    for file in htmls:
        os.remove(file)

if __name__ == "__main__":
	convert_pdf()
