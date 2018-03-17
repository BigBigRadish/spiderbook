#coding:utf-8
import urllib.request
import urllib
import urllib3
import http.cookiejar
from http.cookiejar import CookieJar
response=urllib.request.urlopen('http://www.zhihu.com');
html=response.read();
print(html);
user_agent='Mozilla/5.0 (compatible;MSIE 5.5;Windows NT 10.0) '
url="https://www.zhihu.com/login/email";
referer='https://www.zhihu.com'
postdata={'username':'luozhukun@163.com','password':'lzk15884706478'};
#post信息需要进行编码
data=urllib.parse.urlencode(postdata).encode(encoding='UTF8');#报错:POST data should be bytes or an iterable of bytes. It cannot be of type str
print(data);
headers={
    "Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Accept":"*/*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":"XMLHttpRequest",
    "Connection":"keep-alive"
}
headers1={'User-Agent':user_agent,'Referer':referer};
req=urllib.request.Request(url,data,headers);
response=urllib.request.urlopen(req);
html =response.read();
print(str(html).encode(encoding='utf_8', errors='strict'));
'''
'''
'''
说明：带cookie的打印出来必须用opener.open(req).read().decode('utf-8')来发送的请求才会带上cookie，如果用urllib.request.urlopen()是不带cookie的

 

说明：
1.urllib.request.Request()返回了一个request的请求实例
2.urlopen是一个封装好的OpenerDirector实例，里面只有三个参数（url，data，timeout）
3.通过build_opener可以自己创建一个OpenerDirector实例，所以如果想要构建一个cookie管理
   build_opener(*handlers)，将handler类实例化增加到OpenerDirector中，比如像上面的例子里增加cookie，
 '''
cookie=CookieJar();
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie));
response=opener.open('http://www.zhihu.com/');
for item in cookie:
    print(item.name+'  '+item.value);
    '''
    '''
opener= urllib.request.build_opener();
opener.addheaders.append(('cookie','email='+'luozhukun@163.com'))
req=urllib.request.Request('http://www.zhihu.com');
response=opener.open(req);
print(response.headers);
retdata=response.read();
print(retdata);
