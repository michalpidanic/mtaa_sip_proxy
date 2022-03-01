import time

class Record():
    def __init__(self):
        self.buffer = ""

    def writeToFile(self):
        line = self.buffer
        self.buffer = ""
        with open('history.txt', 'a') as f:
            f.write(line)
            f.write('\n')
            f.close()

    def writeToBuffer(self, data):
        self.buffer += ' '
        self.buffer += data

    def timestamp(self):
        self.buffer += time.strftime("(%H:%M:%S)", time.localtime())