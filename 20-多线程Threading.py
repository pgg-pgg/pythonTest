# from threading import Thread
# import time
#
# def test():
#     print("------昨晚喝多了，下次少喝点")
#     time.sleep(1)
#
# for i in range(5):
#     t=Thread(target=test)
#     t.start()


import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg=self.name+str(i)
            print(msg)


if __name__=='__main__':
    t=MyThread()
    t.start()