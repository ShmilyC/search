import threading
import queue
import time

class AddDataThread(threading.Thread):
    def __init__(self,basewindow,queue):
        super().__init__()
        self.basewin = basewindow
        self.queue = queue
    def run(self):
        for i in range(100):
            try:
                mydata = self.queue.get(block=True,timeout=300)
                self.basewin.adddata(mydata)
            except:
                print('yichang')