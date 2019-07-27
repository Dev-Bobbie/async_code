from __future__ import absolute_import, print_function, unicode_literals
import requests
from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

# 使用task装饰器，注册urlopen函数为task
# ignore_result如果为True，意味着celery不会存储函数的返回结果
@app.task(ignore_result=False)
def urlopen(url):
    print('Opening: {0}'.format(url))
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
        response = requests.get(url,headers=headers)
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as exc:
        print('Exception for {0}: {1!r}'.format(url, exc))
        return "fail", url
    print('Done with: {0}'.format(url))
    # 返回的结果必须是能被json序列化的数据
    # 如unicode类型字符串、数值、含有unicode类型字符串或数值的字典、列表等
    return {"url": url}

if __name__ == '__main__':
    pass