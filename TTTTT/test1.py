
import threading
import time

# 主线程
def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.people = people
        self.threadName = name

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)   # 执行任务
        print("成功")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 守护线程setDaemon(True)
#thread1.setDaemon(True)   # 必须在start之前，作用是：主线程结束后不会继续运行子线程
#thread2.setDaemon(True)

# 开启线程
thread1.start()
thread2.start()

# 必须在start之后，阻塞主线程，等所有子线程结束后，主线程才会结束
thread1.join()
thread2.join()

time.sleep(0.5)
print("退出主线程")