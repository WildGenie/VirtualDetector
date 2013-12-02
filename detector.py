import socket, select,  datetime
from PyQt4 import QtCore

CMD_PORT = 1234
IMG_PORT = 1235
class Channel():
    def __init__(self, port,  parent=None):
        self.socket  = socket.socket()
        self.host = socket.gethostname()
        self.port = port
        self.socket.bind((self.host,  self.port))
        self.socket.listen(1)

        
        
class Detector(QtCore.QThread):
    def __init__(self,  parent = None):   
        QtCore.QThread.__init__(self, parent) 
        self.cmdChannel  = Channel (CMD_PORT)
        self.imgChannel =  Channel (IMG_PORT)
        self.inputs = [self.cmdChannel.socket, self.imgChannel.socket]
        self.cmdChannels = []
        self.imgChannels = []
        self.stopFlag = True;
        self.pixelNum = 8
        self.init_dataPattern()
        self.integrationTime = 100
    def init_dataPattern(self):
        step = 5
        self.data = [i for i in range(0,  step *(self.pixelNum -1),  step)]
        print self.data
        
    def pixelNum(self):
        return self.pixelNum
        
    def setPixelNum(self,  nm):
        self.pixelNum = num
        init_dataPattern()
    def stop(self):
        self.stopFlag = True
        
    def run (self):
        self.stopFlag = False
        self.timetick = datetime.datetime.now().microsecond
        while not self.stopFlag:
            rs, ws, es = select.select(self.inputs, [], [], self.integrationTime)
            for w in ws:
                # img channel for writing
                if w in imgChannels:
                #  send data to client
                    pasttime = abs(datetime.datetime.now().microsecond - self.timetick)
                    if pasttime > self.integrationTime:
                        print "send image data"
                    self.timetick = datetime.datetime.now().microsecond
                    
                
            for r in rs:
                if r is self.cmdChannel.socket:
                    c, addr = self.cmdChannel.socket.accept()
                    print 'Got Cmd connection from', addr
                    self.inputs.append(c)
                    
                    #remove the old cmd connect if there is new comming request
                    for channel in self.cmdChannels :
                        channel.close()
                        self.cmdChannels.remove(c)
                    self.cmdChannels.append(c)
                    
                elif r is self.imgChannel.socket:
                    c, addr = self.imgChannel.socket.accept()
                    print 'Got Img Connection from',  addr
                    self.inputs.append(c)
                    
                    #remove the old cmd connect if there is new comming request
                    for channel in self.imgChannels :
                        channel.close()
                        self.imgChannels.remove(c)
                    self.imgChannels.append(c)
                    
                elif r in self.cmdChannels:
                    #cmd Channel data comming 
                    print "cmd data comming "
                    try:
                        data = r.recv(1024)
                        disconnected = not data
                        print "data is " + data
                    except socket.error:
                        disconnected = True
                    if disconnected:
                        print r.getpeername(), 'disconnected'
                        self.inputs.remove(r)
                    #process data
                    
                    
                    
                elif r in imgChannels:
                    #cmd Channel data comming 
                    print "img data comming Wrong"
                    
