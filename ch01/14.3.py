#coding:utf-8
#coroutine协程
#gevent的使用流程
from gevent import monkey; monkey.patch_all()
import gevent
import urllib.request
def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print ('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)
if __name__=='__main__':
    urls = ['https://github.com/','https://www.python.org/','http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls  ]#spawn()用于形成协程
    gevent.joinall(greenlets)
'''

'''
#gevent pool对象使用
from gevent import monkey
monkey.patch_all()
import urllib.request
from gevent.pool import Pool
def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print ('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print (e)
    return ('url:%s --->finish'% url)
if __name__=='__main__':
    pool = Pool(2)
    urls = ['https://github.com/BigBigRadish','https://www.python.org/','http://www.cnblogs.com/']
    results = pool.map(run_task,urls)
    print (results)