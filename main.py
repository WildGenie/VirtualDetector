#!/usr/bin/python
import sys,  os
from PyQt4 import QtCore, QtGui
from ui_Detector import Ui_Form
from detector import Detector

class DetectorUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.startButton,QtCore.SIGNAL("clicked()"), self.start)
        QtCore.QObject.connect(self.ui.pathButton,QtCore.SIGNAL("clicked()"), self.set_source_file_path)
        QtCore.QObject.connect(self.ui.patternCheckBox,QtCore.SIGNAL("clicked()"), self.patternClicked)
        self.detector = Detector()
        
    def start(self):
        if self.detector.isRunning():
            self.setWindowTitle('Stopped')
            self.detector.stop()
            self.ui.startButton.setText("Start")
        else:
            self.setWindowTitle('Running')
            self.detector.start()
            self.ui.startButton.setText("Stop")
            
    def set_source_file_path(self):
        dir = os.path.dirname(".")
        fileName = QtGui.QFileDialog.getOpenFileName (self,  "Open data file", dir , "Image Files (*.txt)")
        #Todo set the txt file as the data source
        self.ui.pathEdit.setText(fileName)

    def patternClicked(self):
        if self.ui.patternCheckBox.isChecked() :
            #output data pattern
            print "patern enabeled"
        else:
            #output data source
            print "patern disable"
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = DetectorUI()
    myapp.show()
    sys.exit(app.exec_())
    
