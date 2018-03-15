#coding:utf-8
'''
在windows上创建多进程
'''
import os,time,random;
import multiprocessing;
from multiprocessing import Process,Pool,Queue;
def run_process(name):
    print ('child process %s (%s) running...'% (name,os.getpid()));
if __name__ =='__main__':
    print ('current process (%s) start ...'%(os.getpid()));
    for i in range(5):
        p= Process(target=run_process,args=(str(i),));#target表示处理的函数，args表示提供给函数的参数
        print ("process will start");
        p.start();
    p.join();
    print("process end!");
  
'''multiprocess module provide a process pool'''
def run_task(name):
    print ('Task %s (pid = %s) is running...' % (name, os.getpid()));
    time.sleep(random.random() * 3);
    print ('Task %s end.' % name);
if __name__=='__main__':
    print ('Current process %s.' % os.getpid());
    p = Pool(processes=3);
    for i in range(5):
        p.apply_async(run_task, args=(i,));#使用进程池提供的方法进行处理
    print ('Waiting for all subprocesses done...');
    p.close();
    p.join();
    print ('All subprocesses done.');
'''使用queue数据结构进行进程间的通信'''
# 写数据进程执行的代码:
def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid());
    for url in urls:
        q.put(url);
        print('Put %s to queue...' % url);
        time.sleep(random.random());
# 读数据进程执行的代码:
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid());
    while True:
        url = q.get(True);
        print('Get %s from queue.' % url);
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue();
    proc_writer1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']));
    proc_writer2 = Process(target=proc_write, args=(q,['url_4','url_5','url_6']));
    proc_reader = Process(target=proc_read, args=(q,));
    # 启动子进程proc_writer，写入:
    proc_writer1.start();
    proc_writer2.start();
    # 启动子进程proc_reader，读取:
    proc_reader.start();
    # 等待proc_writer结束:
    proc_writer1.join();
    proc_writer2.join();
    # proc_reader进程里是死循环，无法等待其结束，只能强行终止:
    proc_reader.terminate();
'''
pipe 进程间通信，常用于两个进程间通信
'''
def proc_send(pipe,urls):
    for url in urls:
        print ("Process(%s) send: %s" %(os.getpid(),url));
        pipe.send(url);
        time.sleep(random.random());
def proc_recv(pipe):
    while True:
        print ("Process(%s) rev:%s" %(os.getpid(),pipe.recv()));
        time.sleep(random.random());
if __name__=='__main__':
    pipe=multiprocessing.Pipe();
    proc_send1 = Process(target=proc_send, args=(pipe[0],['url_'+str(i) for i in range(10)]));
    proc_recv2 = Process(target=proc_recv, args=(pipe[1],));
    proc_send1.start();
    proc_recv2.start();
    proc_send1.join();
    proc_recv2.terminate();
    

        