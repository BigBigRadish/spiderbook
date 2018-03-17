#coding:utf-8
#Request实现request请求
import requests
r=requests.get("http://www.zhihu.com");
print(r.content);
'''
'''
postdata={'username':'luozhukun@163.com','password':'lzk15884706478'};
r=requests.post('http://www.zhihu.com',data=postdata);
print(r.content)
loginurl="http://www.zhihu.com/login"
s=requests.Session();
r=s.get(loginurl,allow_redirects=True);
data={'username':'luozhukun@163.com','password':'lzk15884706478'}
r=s.post(loginurl, data=data, allow_redirects=True);
print(r.text);