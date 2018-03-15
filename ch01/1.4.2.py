#coding:utf-8
import random
import time,threading
#method1:函数传参创建多线程
def thread_run(urls):
    print ('current %s is running...'%threading.current_thread().name);
    for url in urls:
        print('%s--->>%s'% (threading.current_thread().name,url));
        time.sleep(random.random());
    print('%s ended.'% threading.current_thread().name);
t1 = threading.Thread(target=thread_run,name='thread1',args=(['url1','url2','url3'],));
t2 = threading.Thread(target=thread_run,name='thread2',args=(['url4','url5','url6'],));
print("%s is running..."% threading.current_thread().name);
t1.start();
t2.start();
t1.join();
t2.join();
print('%s ended...'%(threading.current_thread().name));
'''
'''
#method2:继承方式创建多线程
class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls
    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
                print ('%s ---->>> %s' % (threading.current_thread().name,url))
                time.sleep(random.random())
        print ('%s ended.' % threading.current_thread().name)
print ('%s is running...' % threading.current_thread().name)
t1 = myThread(name='Thread_1',urls=['url_1','url_2','url_3'])
t2 = myThread(name='Thread_2',urls=['url_4','url_5','url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print( '%s ended.' % threading.current_thread().name)
'''
'''
#线程同步
mylock = threading.RLock()
num=0
class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        global num
        while True:
            mylock.acquire()
            print ('%s locked, Number: %d'%(threading.current_thread().name, num))
            if num>=4:
                mylock.release()
                print ('%s released, Number: %d'%(threading.current_thread().name, num))
                break
            num+=1
            print ('%s released, Number: %d'%(threading.current_thread().name, num))
            mylock.release()
if __name__== '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()
#多线程适合i/o密集型操作，多进程适合cpu密集型操作
