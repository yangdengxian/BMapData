import threading
import time

threadLock = threading.Lock()


class Thread (threading.Thread):
    def __init__(self, threadId, name, delay, customRun):
        threading.Thread.__init__(self)
        # 线程ID
        self.threadId = threadId
        # 线程名称
        self.name = name
        # 延迟时间
        self.delay = delay
        # 执行函数
        self.customRun = customRun

    def run(self):
        print("Starting " + self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        self.customRun(self.name, self.delay)
        # 释放锁
        threadLock.release()
        print("Exiting " + self.name)


if __name__ == "__main__":
    """ poiTypeThreadsList = ['美食', '酒店', '购物', '生活服务',
                          '丽人', '旅游景点', '休闲娱乐', '运动健身',
                          '教育培训', '文化传媒', '医疗', '汽车服务',
                          '交通设施', '金融', '房地产', '公司企业',
                          '政府机构', '出入口', '自然地物']
    for value in poiTypeThreadsList:
        thread = Thread(poiTypeThreadsList.index(value), value, 0)
        thread.start()

    print("Exiting Main Thread") """
