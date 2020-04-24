"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/6'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from lxml import etree
text = '''
<img alt="出卖本拉登的那位医生，最后是什么下场，5000万赏金得到了么" src="//i2.hdslb.com/bfs/archive/e18ac4e87e8c1668bfa95f5713a46c523edcdf47.jpg@114w_70h.webp">
'''
html = etree.HTML(text)
# 按字符串序列化HTML文档
result = etree.tostring(html)

print(result)
print(html.xpath("//img/@src"))

